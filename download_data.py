import time
import os
import obspy
from obspy.clients.fdsn.mass_downloader import RectangularDomain, \
        Restrictions, MassDownloader


basedir = "./data_repo"
waveform_base = os.path.join(basedir, "waveform")
station_base = os.path.join(basedir, "station")


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        dt = te - ts
        print("%r  %2.2f s" % (method.__name__, dt))
        return {"result": result, "time": dt}
    return timed


def safe_mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def get_event_time(event):
    origin = event.preferred_origin()
    return origin.time


def download_data(starttime, endtime, waveform_dir, station_dir,
                  networks=None, channels=None, providers=None,
                  minimum_length=0.95):
    # Rectangular domain containing parts of southern Germany.
    domain = RectangularDomain(
        minlatitude=-90, maxlatitude=90,
        minlongitude=-180, maxlongitude=180)

    if isinstance(channels, list):
        channel = ",".join(channels)
    elif channels == "None" or channels is None:
        channel = None
    else:
        raise ValueError("Unknown channels: {}".format(channels))

    if isinstance(networks, list):
        network = ",".join(networks)
    elif networks == "None" or networks is None:
        network = None
    else:
        raise ValueError("Unknown networks: {}".format(networks))

    print("network: ", network)
    print("channel: ", channel)

    # Set download restrictions
    restrictions = Restrictions(
        starttime=starttime,
        endtime=endtime,
        reject_channels_with_gaps=False,
        minimum_length=minimum_length,
        station=None,
        network=network,
        channel=channel,
        location_priorities=["", "00", "10"],
        channel_priorities=["BH[ZNE12]", "HH[ZNE12]"]
    )

    if (providers is None) or (providers == "None"):
        mdl = MassDownloader()
    else:
        mdl = MassDownloader(providers=providers)

    mdl.download(domain, restrictions,
                 mseed_storage=waveform_dir,
                 stationxml_storage=station_dir)


@timeit
def download_event(eventname, event, params):
    # Request config_file
    event_time = get_event_time(event)

    obsd_dir = os.path.join(waveform_base, eventname)
    safe_mkdir(obsd_dir)
    station_dir = os.path.join(station_base, eventname)
    safe_mkdir(station_dir)

    starttime = event_time + params["starttime_offset"]
    endtime = event_time + params["endtime_offset"]
    print("event time:   ", event_time)
    print("download time:", starttime, endtime)
    print("providers: ", params["providers"])

    # Get station_list from station_file in database entry
    download_data(starttime, endtime,
                  obsd_dir, station_dir,
                  networks=params["networks"],
                  channels=params["channels"],
                  providers=params["providers"])


def load_test_params():
    params = {
        "starttime_offset": -300,
        "endtime_offset": 11000,
        "networks": ["II", "IU", "IC"],
        "channels": None,
        "providers": None
    }
    return params


def load_prod_params():
    params = {
        "starttime_offset": -300,
        "endtime_offset": 11000,
        "networks": None,
        "channels": None,
        "providers": None
    }
    return params


def main():
    eventname = "C201801210106A"
    eventfile = os.path.join("./cmt", eventname)
    event = obspy.read_events(eventfile)[0]

    params = load_test_params()
    #params = load_prod_params()

    download_event(eventname, event, params)


if __name__ == "__main__":
    main()
