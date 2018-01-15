### Doc 
https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/rest-api/rest-api.pdf 

### how to get the equivalent rpc of a Junos show command:
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
