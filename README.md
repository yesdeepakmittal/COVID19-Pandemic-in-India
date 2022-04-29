# Covid19 Data Visualization
This project is an attempt to visualize the distribution of Covid19 cases chronologically in different states. A [Python web application](https://share.streamlit.io/yesdeepakmittal/covid19-pandemic-in-india/app.py) is also made using Streamlit framework. 

## How to use it?
- Install latest version of [Python](https://www.python.org/downloads/)
- Make a [Virtual Environment](https://gist.github.com/yesdeepakmittal/61494217c8be4a7e61524e27824943bd) and activate it.
- Clone this repository `git clone https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India.git`
- `cd COVID19-Pandemic-in-India`
- `pip install -r requirements.txt`
- run application using `streamlit run app.py`
- Check your application in the browser at `http://localhost:8501` 

## Docker Image
The Docker image is available at [DockerHub](https://hub.docker.com/r/yesdeepakmittal/covid19-pandemic-in-india). This image gets automatically updated for every `push` or `pull_request` to this repository using GitHub Actions. 

## Want to run Docker Image?
- Log in on [Play with Docker](https://labs.play-with-docker.com/) by signing in using Docker ID
- Create a new instance
- Run the following commands
```
docker pull yesdeepakmittal/covid19-pandemic-in-india:latest
docker run -it yesdeepakmittal/covid19-pandemic-in-india:latest /bin/sh
pip install streamlit
streamlit run app.py
```

## Overview

<div><img src="img/2.png" alt="" width="700" height="500"></div>
<div><img src="img/3.png" alt="" width="700" height="500"></div>
<div><img src="img/4.png" alt="" width="700" height="500"></div>
<div><img src="img/5.png" alt="" width="700" height="500"></div>
<div><img src="img/8.png" alt="" width="700" height="500"></div>
<div><img src="img/9.png" alt="" width="700" height="500"></div>
<div><img src="img/10.png" alt="" width="700" height="500"></div>

## Support
- Please contribute to the project by adding new functionality and opening a pull request
- For any support/clarification to configure this project, consider opening an [Issue](https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India/issues/new)
