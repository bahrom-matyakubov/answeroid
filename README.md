# answeroid

A simple bot for helping on Q/A sites

## Setup instructions (linux):
1) Download and install [python](https://www.python.org/), [virtualenv](https://virtualenv.pypa.io/en/stable/) (optional, but strongly recommended), and [pip](https://pypi.python.org/pypi/pip).

2) Get a Wolfram AppID from [Wolfram|Alpha Developer Portal](https://developer.wolframalpha.com/portal/myapps/):
  * Sign into the portal (sign up if you don't have an account already).
  * Click on "Get an AppID"
  * In the popup, fill in the Application Name and Description fields, and click on ***Get AppID***
  * You should now see a ***Your AppID Has Been Created*** prompt with the following fields:
    - APP NAME: *the name you have entered*
    - APPID: **XXXXXX-XXXXXXXXX** - take a note of this app id
    - USAGE TYPE: Personal/Non-commercial Only
  * If you closed the popup before taking down the app id, you can find it again in the [developer portal](https://developer.wolframalpha.com/portal/myapps/index.html). Just click on ***Edit*** under the corresponding app.
  * Now that you have your app id, store it in an environment variable named `WOLF_APP_ID`. You can add it to your profile in order to avoid having to re-export it on every reboot - just add `export WOLF_APP_ID='XXXXXX-XXXXXXXXX'` (replace with your app id) to `~/.profile`. At the time of writing, a free app id allows you 2,000 queries per month per app.

3) (*Note, if you are planning on contributing to answeroid, please skip this step*) Install the required dependencies:
   1. Create folder for your project: `mkdir answeroid`
   2. <a name="3-2">Create a virtual environment inside the project folder: `cd answeroid && virtualenv -p python3 ve`</a>
      - `-p` allows you to specify the python executable, this project uses Python 3
      - `ve` is just the name of your virtual environment - you can make it more descriptive, but I tend to use `ve` - short for virtual environment of said project, since it's inside the `project_folder` anyway
   3. <a name="3-3">Activate the created virtual environment: `source ve/bin/activate`</a>
      - You should see a `(ve)` (or the name of your virtual environment if you used something other than `ve`) prepended to your shell prompt. If not please double check the steps above.
   4. With the virtual environment active, install answeroid: `pip install answeroid`. This will download answeroid along with all of its dependencies.

4) If you are going to contribute to ***answeroid***, instead of downloading it from pip, you will have to [fork this repository](https://help.github.com/articles/fork-a-repo/). Once you have forked the repo and cloned your fork, install the dependencies:
   1. Follow the steps [3-2](#3-2) and [3-3](#3-3) above
   2. With the virtual environment active, install all the required dependencies: `pip install -r requirements.txt`. This will download all the dependencies needed to run answeroid.
   
5) To run the bot (*I'm working on incorporating this bot into a Slack team chat, so a concrete example should be available soon*):
   1. Create a subclass of `Site`.
      - The idea is that, when deployed, the bot monitors your activity on said `Site` by periodically calling [`get_viewing_question`](https://github.com/bahrom-matyakubov/answeroid/blob/68b0df82dbdd5322a2d92c4e329a3a28a639e98c/sites/common.py#L30) and scanning your replies on that question. When it finds relevant replies (i.e. `WOLF: query`, `BING: query`, or `GCAL: query`), it sends the `query` to the corresponding provider, and edits your reply with the results from the given provider
   2. Update the import statement in [main](answeroid/answeroid/main.py). Instead of importing `Site` from `sites.common` import your subclass from the module where it is located and update the [`with` clause](https://github.com/bahrom-matyakubov/answeroid/blob/68b0df82dbdd5322a2d92c4e329a3a28a639e98c/answeroid/main.py#L16) accordingly.
   3. With the virtual environment still active, run [main](answeroid/answeroid/main.py): `(ve) _____ $ python answeroid/main.py` (assuming you're in the root directory of the project)

## Deployment instructions ([raspbian](https://www.raspberrypi.org/downloads/raspbian/)):
1) *Coming soon*
