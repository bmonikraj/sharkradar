# SharkRadar
**Sharkradar** is a lightweight, yet flexible **service registry and discovery** tool, compatible with any microservice *(independent of tech stack)*, as long as your microservice supports **HTTP** for communication (generally, it surely would, unless you have some custom protocol for communication. In that case, *Congratulations* !)

Sharkradar **is**
:heavy_check_mark: Service (RD) registry and discovery
:heavy_check_mark: HTTP based service 
:heavy_check_mark: Compatible with any microservice 
:heavy_check_mark: Weighted priority discovery
:heavy_check_mark: Service which tells you the address of *best* instance of server which can handle your request
:heavy_check_mark: Can register/discover heterogenous instances (of microservices) and homogenous instances

Sharkradar is **not**
:x: API Gateway
:x: Not a router to redirect requests
:x: Not a proxy/reverse-proxy
:x: A poller which will check if the services are up. It only knows if services are up, only when service tells itself

## Architecture
The architecture of sharkradar is pretty straight forward, keeping in mind:

 - Usability
 - Compatibility
 - Lightweight
 - Low storage footprint
 - Low computational footprint
 
![Architecture](https://drive.google.com/uc?id=19wH9r_8AU4gkSgNn-n-iT8IL0mpNZodX)

**The fundamental principle behind the architecture is a "publish/ask" mechanism** 

> **Service R(registry)** => "You *(microservices/applications/consumers)* give me your fitness report. If I receive, I will give you work to do based on your ability, I am not gonna ask you for it :no_mouth:. And if I don't receive it within time, you will not be considered for work until next report"

> **Service D(discovery)** => "You want to know which of person can do the job in best way and how to reach him, ask me! I will tell you best person's address, ONLY :neutral_face:. I am not gonna take you there"

**Service Registration**
 - Client (Microservice - who wants to be discoverable through shark radar)
 - Client sends a health report with `params` to shark radar at some decided `frequency` in every last report sent. 
 - If sharkradar doesn't receive the health report, after the threshold time provided by client in previous report, the client is removed from the list of registered services *(hence won't be considered for discovery)*
 - Auto-deregistration happens, if health report is not sent.
 - No separate API / endpoint for registration. First health report will be considered as regitration.

**Service Discovery**

 - Any client (with any tech stack) which understands and able to communicate to HTTP, can ask for a service location (*IP address* and *Port*) 
 - The address given is for the best (selected by a weight based priority algorithm) client with the asked `service name`
