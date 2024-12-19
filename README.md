# TIE Dataset

The TIE(Technical Indian English) dataset is a massive speech dataset of ~750 GB, consisting of ~9.8K technical lectures in English, along with their transcripts. The lectures were delivered by instructors from all over India and were sourced from the NPTEL website. The dataset can be requested here:[https://forms.gle/k4A6kW8gRZ7qJiJB9]. 

The shorter version of TIE audio files along with aligned ground-truth transcripts is also available at [![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)](https://huggingface.co/datasets/raianand/TIE_shorts).


## Folder Structure

- `Final_Dataset.csv`: CSV file containing metadata corresponding to the audio, including gender, caste, region, speech rate, age group, and discipline group.

- `Final_Transcripts`: This folder contains transcripts corresponding to each audio. Each audio has three sets of transcripts:
  - `{Audio_ID}_manual`: Manually transcribed transcript.
  - `{Audio_ID}_auto`: YouTube automatic caption generated transcript.
  - `{Audio_ID}_whisper_base`: OpenAI Whisper generated transcript.

- `Final_Dataset_audios`: This folder contains all the audio files in the dataset.

## Usage

- To access and utilize this dataset, you can download it from Google Drive using the provided link. As the audio dataset is substantial in size, you have the option to download only a subset of audios by using the script download_video.py. This way, you can manage the data more efficiently and select specific portions of the dataset that align with your research or project needs. 

- The `Final_Dataset.csv` file provides metadata for each audio in the dataset.

- The `Final_Transcripts` folder contains various transcripts associated with each audio.

## License

Attribution-ShareAlike 2.0 Generic (CC BY-SA 2.0) 


## Datasheet

The detailed datasheet based on [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper is available [here](https://github.com/raianand1991/TIE/blob/main/datasheet-for-dataset-template.md)

## Attribution

If you use this dataset in your research or projects, please cite this repository as follows:

@article{rai2023deep,
  title={A Deep Dive into the Disparity of Word Error Rates Across Thousands of NPTEL MOOC Videos},
  author={Rai, Anand Kumar and Jaiswal, Siddharth D and Mukherjee, Animesh},
  journal={arXiv preprint arXiv:2307.10587},
  year={2023}
}

## Contact

For any inquiries, feedback, or collaboration opportunities, please contact [raianand.1991@gmail.com].

---



