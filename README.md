# Repository documentation structure

- [**What to find in this repository**](README.md#what-to-find-in-this-repository)
- [**How to get locally the content of the remote repository**](README.md#what-to-find-in-this-repository)
- [**JUNOS**](README.md#junos)
- [**JUNOS SPACE**](README.md#junos-space)

# What to find in this repository

REST calls examples for Juniper solutions.

# How to get locally the content of the remote repository

```
sudo -s
git clone https://github.com/ksator/rest_calls_to_juniper.git
cd rest_calls_to_juniper/
```
You can now use the local copy of this remote repository.  


# JUNOS

### Junos REST API guide
https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.pdf 

### RPC

Each junos show command has an equivalent rpc.   
To get the equivalent rpc of a Junos show command, add ```| display xml rpc``` at the end of the show command.  
Run this command to get the equivalent rpc of ```show version``` (which is ```get-software-information```):
```
lab@spine-03> show version | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.3R1/junos">
    <rpc>
        <get-software-information>
        </get-software-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

Some show commands use arguments, so the equivalents rpc require arguments:  
Run this command to get the equivalent rpc of ```show chassis hardware clei-models```:
```
pytraining@mx80-17> show chassis hardware clei-models | display xml rpc 
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/17.2R1/junos">
    <rpc>
        <get-chassis-inventory>
                <clei-models/>
        </get-chassis-inventory>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

Run this command to get the equivalent rpc for ```show route receive-protocol bgp 192.168.10.4 active-path hidden```:
```
pytraining@newhostname> show route receive-protocol bgp 192.168.10.4 active-path hidden | display xml rpc    
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/12.3R11/junos">
    <rpc>
        <get-route-information>
                <active-path/>
                <bgp/>
                <peer>192.168.10.4</peer>
                <hidden/>
        </get-route-information>
         </rpc>
        <cli>
            <banner>{master:0}</banner>
        </cli>
    </rpc-reply>
```

### Enable REST API on Junos

Run these commands to enable REST API on Junos.  
The default port is 8080.  

The below commands enable also a graphical REST API Explorer that allow to conveniently experiment with REST APIs.   

```
lab@dc-vmx-3> show configuration system services rest | display set
set system services rest http port 8080
set system services rest enable-explorer
```

### Junos REST API explorer

### curl

### Python 

# JUNOS SPACE
The python scripts [junos_space.py](junos_space/junos_space.py) extracts and prints the ip addresses of all EX4300-48T from junos space

```
python junos_space/junos_space.py
```
The output is ip address of EX4300-48T devices from junos space: 
```
172.30.108.138
172.30.108.134
```
