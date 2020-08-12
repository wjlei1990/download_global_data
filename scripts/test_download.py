import os
import obspy
from download_util import download_event


def load_test_params():
    params = {
        "starttime_offset": -600,
        "endtime_offset": 11000,
        "networks": ["FR"],
        "channels": None,
        "location_priorities": ["", "00", "10"],
        "channel_priorities": ["BH[ZNE12]", "HH[ZNE12]"],
        #"channel_priorities": ["BH[ZNE12]"],
        "providers": None
    }
    return params


def load_prod_params():
    params = {
        "starttime_offset": -600,
        "endtime_offset": 11000,
        "networks": None,
        "channels": None,
        "location_priorities": ["", "00", "10"],
        "channel_priorities": ["BH[ZNE12]", "HH[ZNE12]"],
        #"channel_priorities": ["BH[ZNE12]"],
        "providers": None
    }
    return params


def main():
    eventname = "C201801210106A"
    eventfile = os.path.join("../CMT/CMT.360", eventname)
    event = obspy.read_events(eventfile)[0]

    #params = load_test_params()
    params = load_prod_params()

    #basedir = "./test_data_repo"
    basedir = "/gpfs/alpine/geo111/proj-shared/wenjie/data/raw_obsd/"
    waveform_base = os.path.join(basedir, "waveform")
    station_base = os.path.join(basedir, "station")

    download_event(eventname, event, params, waveform_base, station_base)


if __name__ == "__main__":
    main()
