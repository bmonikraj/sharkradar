# SharkRadar

![Travis (.org)](https://img.shields.io/travis/bmonikraj/sharkradar) ![Coveralls github](https://img.shields.io/coveralls/github/bmonikraj/sharkradar) [![GitHub license](https://img.shields.io/github/license/bmonikraj/sharkradar)](https://github.com/bmonikraj/sharkradar/blob/master/LICENSE.rst) ![PyPI](https://img.shields.io/pypi/v/sharkradar) ![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/bmonikraj/sharkradar)

**Sharkradar** is a lightweight, yet flexible **service registry and discovery** tool, compatible with any microservice *(independent of tech stack)*, as long as your microservice supports **HTTP** for communication (generally, it surely would, unless you have some custom protocol for communication. In that case, *Congratulations* :D !)

## Installation 
```python
pip install sharkradar
```

## Usage
```python
sharkradar --help
```

## Technical Documentation
[**Complete Technical Documentation available here, on project's wiki**](https://github.com/bmonikraj/sharkradar/wiki)

## Overview
Sharkradar **is** <br/>
- Service (RD) registry and discovery <br/>
- HTTP based service <br/>
- Compatible with any microservice <br/>
- Weighted priority discovery <br/>
- Service which tells you the address of *best* instance of server which can handle your request <br/>
- Can register/discover heterogeneous instances (of microservices) and homogeneous instances <br/>

Sharkradar is **not** <br/>
- API Gateway <br/>
- Not a router to redirect requests <br/>
- Not a proxy/reverse-proxy <br/>
- A poller which will check if the services are up. It only knows if services are up, only when service tells itself <br/>

## Technical Requirements

 1. OS - Any OS which supports Python :D
 2. Dependency - Python (>=3 is preferred)
 3. Networking - similar to any other microservice/server (like exposing ports, IP address binding, etc). Must be reachable by all the services using sharkradar
 4. Any specific module/library/agent for Client/Microservices using Sharkradar - **NO** (Only a HTTP communication library/ability to make HTTP GET, PUT calls :D)
 5. Reachability - Sharkradar **must be reachable** by all the clients/microservices/services using sharkradar (network administrators, please take a note :D)
 6. Availability - Sharkradar is a standalone application, *for now!*. So sharkradar could be the single point of inter-microservice communication, and also single point of failure (of inter microservice communication)

## Architecture
The architecture of sharkradar is pretty straight forward, keeping in mind:

 - Usability
 - Compatibility
 - Lightweight
 - Low storage footprint
 - Low computational footprint
 
![Architecture](https://drive.google.com/uc?id=19wH9r_8AU4gkSgNn-n-iT8IL0mpNZodX)

**The fundamental principle behind the architecture is a "publish/ask" mechanism** 

> **Service R(registry)** => "You *(microservices/applications/consumers)* give me your fitness report. If I receive, I will give you work to do based on your ability, I am not gonna ask you for it :(. And if I don't receive it within time, you will not be considered for work until next report"

> **Service D(discovery)** => "You want to know which of person can do the job in best way and how to reach him, ask me! I will tell you best person's address, ONLY -_-. I am not gonna take you there"

**Service Registration**
 - Client (Microservice - who wants to be discoverable through shark radar)
 - Client sends a health report with `params` to shark radar at some decided `frequency` in every last report sent. 
 - If sharkradar doesn't receive the health report, after the threshold time provided by client in previous report, the client is removed from the list of registered services *(hence won't be considered for discovery)*
 - Auto-deregistration happens, if health report is not sent.
 - No separate API / endpoint for registration. First health report will be considered as regitration.

**Service Discovery**

 - Any client (with any tech stack) which understands and able to communicate to HTTP, can ask for a service location (*IP address* and *Port*) 
 - The address given is for the best (selected by a weight based priority algorithm) client with the asked `service name`

## Contribution | Issues or Bugs | Suggestions
- For *contribution*, fork the repository, develop and create Pull request with `master` branch 
- For *Issue and bug reporting*, create a Issue on the repository, we or our fellow developer community will definitely look into it. And if you win the race and solve the bug, don't hesitate to take the credit by raising a pull request.
- For *suggestions and features*, send a mail to the maintainer. Have already developed the feature, even better. Create a pull request for the same. Our maintainers will review the same and merge it :)

## Maintainers
[Monik Raj Behera](https://github.com/bmonikraj) - [bmonikraj@gmail.com](mailto:bmonikraj@gmail.com) <br/>
[Preetam Nahak](https://github.com/preetamnahak007) - [preetamnahak@gmail.com](mailto:preetamnahak@gmail.com)
