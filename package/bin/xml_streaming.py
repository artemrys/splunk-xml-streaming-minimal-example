import calendar
import datetime
import json
import sys
import xml.sax.saxutils as xss

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


evt_fmt = (
    "<stream><event><host>{0}</host>"
    "<source><![CDATA[{1}]]></source>"
    "<sourcetype><![CDATA[{2}]]></sourcetype>"
    "<time>{3}</time>"
    "<index>{4}</index><data>"
    # "<![CDATA[{5}]]></data></event></stream>"  # old version
    "{5}</data></event></stream>"  # new version
)


def run():
    events = []
    event1 = evt_fmt.format(
        "localhost",
        "my_computer",
        "test:sourcetype",
        calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
        "main",
        xss.escape(json.dumps([{"Data": "Sample1"}, {"Data": "Sample2"}])),
    )
    event2 = evt_fmt.format(
        "localhost",
        "my_computer",
        "test:sourcetype",
        calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
        "main",
        xss.escape("let's see what we will have here"),
    )
    event3 = evt_fmt.format(
        "localhost",
        "my_computer",
        "test:sourcetype",
        calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
        "main",
        xss.escape("<data>hello world</data>"),
    )
    event4 = evt_fmt.format(
        "localhost",
        "my_computer",
        "test:sourcetype",
        calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
        "main",
        xss.escape(json.dumps({"hello": "world"})),
    )
    events.append(event1)
    events.append(event2)
    events.append(event3)
    events.append(event4)

    import remote_pdb; remote_pdb.RemotePdb(host='0.0.0.0', port=4444).set_trace()

    for event in events:
        sys.stdout.write(event)
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
