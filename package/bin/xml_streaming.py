import sys

SCHEME = """<scheme>
    <title>XML Streaming minimal example</title>
    <description>XML Streaming minimal example.</description>
    <use_external_validation>true</use_external_validation>
    <streaming_mode>xml</streaming_mode>
    <use_single_instance>false</use_single_instance>
    <endpoint>
        <args>
            <arg name="name">
                <title>Name</title>
                <description>Name of the input.</description>
            </arg>
        </args>
    </endpoint>
</scheme>
"""


def do_scheme():
    print(SCHEME)


def run():
    events = """<stream>
  <event>
    <time>1654887496</time>
    <data>event_status="(0)The operation completed successfully."</data>
  </event>
  <event>
    <time>1654887496</time>
    <data>event_status="(1)The operation completed successfully."</data>
  </event>
</stream>"""

    sys.stdout.write(events)
    sys.stdout.flush()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--scheme":
            do_scheme()
        elif sys.argv[1] == "--validate-arguments":
            pass
    else:
        run()

    sys.exit(0)
