# Multimodal AI Essentials

Welcome to the "[Multimodal AI Essentials](https://www.oreilly.com/live-events/multimodal-ai-essentials/0642572002285)" code repository! In this repo, we will learn how multimodal AI merges text, image, and audio for smarter models.

Much of the code in these sessions will be featured in the 2nd edition of [my latest book on LLMs](https://a.co/d/ckinlUl):

<div align="center">
    <a href="https://a.co/d/ckinlUl">
        <img src="images/book.jpg" width="150" alt="A Quick Start Guide to LLMs">
    </a>
</div>

So if you're itching for more, check it out and please leave a rating/review to tell me what you thought :)

For even more, check out my [Expert Playlist](https://learning.oreilly.com/playlists/2953f6c7-0e13-49ac-88e2-b951e11388de)!

## Prerequisites


- Intermediate - Advanced Python Skills: Comfort with Python is crucial as we'll be using it throughout the course to interact with Hugging Face tools and integrate NLP into practical examples.

- Foundational Machine Learning Knowledge: You should have an understanding of core machine learning principles, as we’ll build upon these concepts when exploring advanced NLP techniques.nologies in dynamic and evolving data environments.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have set the following api keyes:

- OpenAI key

You're all set to explore the notebooks!

## Usage - Jupyter Notebooks

This project contains several Jupyter notebooks each focusing on a specific topic:

1. **[Intro to Multimodality](https://colab.research.google.com/drive/1zYSzDuYFa_cbRlti3scUjfmvradK8Sf4?usp=sharing)**: An introduction to multimodality with CLIP and SHAP-E

	- **[Whisper](https://colab.research.google.com/drive/1KxLWEEBtgix4zgP52pnxlIoJrZ8sHEYC?usp=sharing)**: An introduction to using Whisper for audio transcription

	- **[Llava](https://colab.research.google.com/drive/1IwNAz1Ee4YUSRNCU-SOsa7FS8Q2vmpoL?usp=sharing)**: Using an open source mult-turn multimodal engine

	- [**Multimodal Semantic Search**](https://colab.research.google.com/drive/1aUz0FKQDSAyXyhRyvkkRsSy7S30mpRJc?usp=sharing): Using SigLip model to build an image search system


2. **Visual Q/A** - This case study requires you to [download the data from my Dropbox here](https://www.dropbox.com/scl/fo/w6iyfox8gnflvm7g10n47/AB47L7tNEl2Q8eyemZa2GMA?rlkey=v9s8bv6cmjukykpilzimswar0&st=fbulzw4e&dl=0). The code snippets should download them in code if that is easier! Our goal is to emulate the process done by [Llama 3.2-Vision-Instruct](https://colab.research.google.com/drive/1r6Nab2L7rYUBV5e8K8u8EFw98adJu5uh?usp=sharing): one of Meta's latest Llama models that can take in images.
	
	- Method 1: BERT + ViT -> GPT-2 (Fusion)

		- Constructing and Training our model: [Local](notebooks/constructing_a_vqa_system.ipynb) and notebook in [Colab](https://colab.research.google.com/drive/1zvbruS1DvFrVgXjNouSrrF9-PphKLWWl?usp=sharing)
		- Using our VQA system: [Local](notebooks/using_our_vqa.ipynb) notebook and [Colab](https://colab.research.google.com/drive/16GOBndQuIBO-UfXdpPte-PXaZS2nsW1H?usp=sharing)
	
		- Method 2: BERT + ViT -> GPT-2 (Fusion)
			- [Train the VQA Model](https://colab.research.google.com/drive/1DSh8_yfubuu5xPVM2BQ-I_eH5rrxLKZU?usp=sharing) and [use it here](https://colab.research.google.com/drive/1AWAk7NTvgTbjktUNB6bmS6T37bgTzRgt?usp=sharing)

3. **Diffusion** - Exploring Diffusion Models and Fine-tuning techniques like Dreambooth

	- **[Intro to Diffusion (StableDiff + Flux)](https://colab.research.google.com/drive/1EtvcJGs_LdcQfSkbffKWKut8Zk7fccCX?usp=sharing)**: Generating images using diffusion models

	- **[Dreambooth](https://colab.research.google.com/drive/1tQt1pE6l0MI79W8ZX0MMu0YVmF2I0GB3?usp=sharing)**: Fine-tuning a stable difusion model to make images of yours truly! Ever wonder what I look like blonde? Me neither but AI gave me some ideas of what it would look like.

4. **Texth to Speech** - Fine-tune text to speech models

	- **[Fine-tuning SpeechT5 to speak Turkish](https://colab.research.google.com/drive/1ZWW2HjvywU48ExX22ZgkZ56MJ50uD4tS?usp=sharing)**: An example of proper SpeechT5 fine-tuning with 150k> high quality audio and transcrption examples
	- **[Fine-tuning SpeechT5 to speak like Sinan](https://colab.research.google.com/drive/1CVdyEvBq-7uerFLOmKPolcT3Z8J2rhAm?usp=sharing)**: I grab videos of me from Youtube, extract the audio, run it through OpenAI's whisper to make my own dataset to train the model to sound more like me

5. **Multimodal Applications**

	- [A Sample Twilio App for Voice Messaging with AI](flask/README.md)

	- [Livekit + Deepgram + OpenAI for a voice to voice assistant](voice-to-voice/README.md)

	- [Multimodal Agents](notebooks/Visual%20Agent.ipynb) - Connecting an agent framework with OpenAI's Dall-E 3 diffusion model

6. **Multimodal Evaluation + Ethics**

	- [Llava-Critic Demo](https://colab.research.google.com/drive/1y0SCzTrjAI0KHp_TxWlkfSCuQYnfbeHM?usp=sharing) - Multimodal LLM (LMM) as a judge
	- [Wav2Lip Demo](https://colab.research.google.com/drive/1nlhVZvi_s2jXpG864r3_NohrjyHG5V7j?usp=sharing) - See how modern deepfakes get made. Also find out my favorite movie! If you believe the video you see that is ;) 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Book time with me on Intro!
If you have questions, I'm available on [Intro](https://intro.co/sinanozdemir) :) 

<div style="text-align: center;">
    <a href="https://intro.co/sinanozdemir">
        <img src="images/intro.png" width="300" alt="Book time with me on Intro">
    </a>
</div>
