<a href="https://livekit.io/">
  <img src="./.github/assets/livekit-mark.png" alt="LiveKit logo" width="100" height="100">
</a>

# Python Voice Agent

<p>
  <a href="https://docs.livekit.io/agents/quickstarts/voice-agent/"><strong>I am following this tutorial</strong></a>. This is a basic example of a voice agent using LiveKit and Python.</p>
  
You need an [OpenAI API Key](https://platform.openai.com/api-keys) and [Deepgram API Key](https://console.deepgram.com/) to go through this tutorial.


# Steps

## Step 1: Install the LiveKit CLI

Create an account or sign in to your [LiveKit Cloud account.](https://cloud.livekit.io/login)

[Install the LiveKit CLI](https://docs.livekit.io/home/cli/cli-setup/) and authenticate using `lk cloud auth`

## Step 2: Bootstrap an agent from template


Clone the starter template for a simple Python voice agent:

```lk app create --template voice-pipeline-agent-python```


Enter your API keys when prompted

## Step 3: Start your Agent

### Start the Backend

Start the backend agent (the agent.py file is what you will change for prompting)

```
cd <agent_dir>

python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
python3 agent.py dev
```

### Start the Frontend

Install dependencies and start your frontend application:

```
cd <frontend_dir>

pnpm install
pnpm dev
```

## Launch your app and talk to your agent!

Visit your locally-running application (by default, [http://localhost:3000](http://localhost:3000))

Select Connect and start a conversation with your agent.
