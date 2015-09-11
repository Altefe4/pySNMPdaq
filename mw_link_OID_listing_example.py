#################################################
# Example config for two Ericsson MINI-LINK TNs #
#################################################
#
# 'ID', 'IP',  and 'OID_dict' are mandatory. Additional keys may
# be added if needed.
#

mw_link_list = \
[{'ID': u'AB1234_AB2345',
  'IP': u'172.123.456.789',
  'OID_dict': {'RX_far': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.10.2129920257',
               'RX_near': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.10.2146697473',
               'TX_far': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.1.2129920257',
               'TX_near': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.1.2146697473'},
  'protection': False,
  'slot': '2'},
 {'ID': u'CD4321_CD3445',
  'IP': u'172.123.456.788',
  'OID_dict': {'RX_far': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.10.2129920257',
               'RX_near': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.10.2146697473',
               'TX_far': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.1.2129920257',
               'TX_near': '.1.3.6.1.4.1.193.81.3.4.3.1.3.1.1.2146697473'},
  'protection': False,
  'slot': '2'}]