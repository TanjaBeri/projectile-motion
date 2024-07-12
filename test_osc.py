"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from pythonosc.osc_message_builder import OscMessageBuilder
import json
import pprint

def print_data(address, *data):
    print(f"Address:{address}")
    print(f"Data: {data}")


if __name__ == "__main__":
  dispatcher = Dispatcher()
  dispatcher.map("/vicon/marker/Teniska_loptica/Sfera*", print_data)

  server = osc_server.ThreadingOSCUDPServer(
      ("", 7000), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()


  msg = {
      "vicon":
          {
              "marker":
                  {
                      "KartonskaKutija":
                              {
                                "Segment1": [1,1,1],
                                "Segment2": [2,3,5],
                                "Segment3": [4,4,4]
                               }
                          
                  }
          }
  }
