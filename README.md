# IP-cyberattack-visualization

**Disclaimer**

Most of the code of this project is taken from https://github.com/MatthewClarkMay/geoip-attack-map which is made by MatthewClarkMay 

What I have changed are some debugged codes due to upgrades and expired websites and using my own data set that is stored in an elasticsearch server rather than generating dummy traffic. 

### Ubuntu 
This project requires an Ubuntu 20.04 which uses python3.8.

### Configurations
- Use you own Mapbox API access token which can be geernated for free to maintain the map - can change that in the map.js file in AttackMapServer --> static --> map.js
- Change root access to the data generation python file if you wish to replace it without another of your own 
- Remember, this code will only run correctly in a production environment after personalizing the parsing functions. The default parsing function is only written to parse gen_data.py traffic.**

### Set up: the code is mostly taken from MatthewClarkMay's github

### Deploy example
Tested on Ubuntu 20.04 LTS.

* Download the files of this github:

* Install system dependencies:

  ```sh
  sudo apt install python3-pip redis-server

  ```

* Install python requirements:

  ```sh
  cd geoip-attack-map
  sudo pip3 install -U -r requirements.txt

  ```
  
* Start Redis Server:

  ```sh
  redis-server
  ```
* Configure the Data Server DB:
  
  ```sh
  cd DataServerDB
  ./db-dl.sh
  cd ..

  ```
* Start the Data Server:

  ```sh
  cd DataServer
  sudo python3 DataServer.py

  ```
  
* Start the Data Generation Script inside DataServer directory:

  * Open a new terminal tab (Ctrl+Shift+T, on Ubuntu).
  
    ```sh
    python3 gen_data.py
    ```
 
* Start the Attack Map Server:
  
    ```sh
    sudo python3 AttackMapServer.py
    ```
 
* Access the Attack Map Server from browser:

    * [http://localhost:8888/](http://localhost:8888/) or [http://127.0.0.1:8888/](http://127.0.0.1:8888/)
  
 
