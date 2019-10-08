# tweetops
A twitter integration pack to HPE composable fabric manager
- a demonstration. Tweet a vlan with the format `vlan-10`

or `vlan-1-6,7,8-10`

Is a stackstorm pack that has a workflow to search twitter and if the world `vlan`
is discovered it checks the screen_name for a match. If matched, it processes a vlan for
sending to the HPE-CFM controller.
