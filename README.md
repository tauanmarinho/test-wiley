# test-wiley-python

## Description

- Test Framework in Python that runs a suite of selenium test, target https://teamshift-qa.crossknowledge.com web page, that ensure the Login page is working as expected, successfully logging in with username and password.

- For this approach, some concepts and open-source testing framework were used to complete.

- Framework created:
    - Validation Login Page of CrossKnowledge
    - Total of methods test: 1
        - Credential validation test: 1 variations
        - Total of tests: 1
    - Expected result: 100% pass - 0% fail
    
## Usage

- Before running:
    
    - Docker installed
    - Run the Zalenium Grid Frame on port 5555:
        ```bash
        docker run --rm -ti --name zalenium -p 5555:4444 -e PULL_SELENIUM_IMAGE=true -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/videos:/home/seluser/videos --privileged dosel/zalenium start
        ```
        or simply run the docker compose:
        ```bash
        docker-compose -f docker-compose.yml up
        ```
    - Find your local ip by:
            - MacOs/Linux: ifconfig
            - Windows: ipconfig

- Run locally:

    - Python 3.8 installed
    
    Inside the src folder, by command line, run the following command:

    ```bash
    python LoginLocally.py
    ```
  
    or also run the test locally with selenium remote, replacing in the code the IP address on line 13 - LoginRemote.py:
  
    ```bash
    python LoginRemote.py
    ```
   
- Run in a docker container:

    Run the following command:

    ```bash
    docker build -t test-wiley . && docker run test-wiley
    ```

- Results, dashboard and Live Preview:

    - [Grid Console URL](http://localhost:5555/grid/console)
    - [Zalenium Live Preview](http://localhost:5555/grid/admin/live?only_active_sessions=true&refresh=60)
    - [Zalenium Dashboard](http://localhost:5555/dashboard/)

## Dependencies
- seleniumhq: 3.9.1

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Manual validation on progress bar

    - Test Cases:
    
        - Pre-conditions:
            Access to internet
            Browser - Firefox/chrome - instaled
            Logged on the https://teamshift-qa.crossknowledge.com by a user already sign up
            
        - Pos-conditions:
            Log off https://teamshift-qa.crossknowledge.com
            
        - [UI][Progress Bar] Validate contents and icons tabs
            
            - Steps:
                1 - Click on the progress bar. Expected: It will open the progress bar on the right side of the broser
                2 - Validate all icons and content of each tab. Expected: Know yourself, Understand your colleagues, Discover your Team Profile, Turn differences into strengths, Make it happen
            
        - [UI][Progress Bar] Validate elements clickable
                    
            - Steps:
                1 - Click on the progress bar. Expected: It will open the progress bar on the right side of the broser
                2 - Validate all tabs clickable. Expected: All the tabs must be clickable
            
        - [UI][Progress Bar] Validate dropdown tabs
                    
            - Steps:
                1 - Click on the progress bar. Expected: It will open the progress bar on the right side of the broser
                2 - Click on each tab. Expected: The arrow that was pointing down, goes up. A list of elements clickable as dropdown appears. Never more than one dropdown appears, even clicking in another tab
            
        