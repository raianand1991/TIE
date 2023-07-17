# TIE Dataset

This repository contains the curated massive speech dataset of 8740 hours consisting of ~9.8K technical lectures in the English language along with their transcripts delivered by instructors representing various parts of Indian demography , sourced from NPTEL website(https://nptel.ac.in/). The dataset can 
be accessed through the Google Drive Link: https://drive.google.com/drive/folders/1k-S61-acXxLyV8jIx-yoGfCTqDzz99EW?usp=sharing

## Folder Structure

- `Final_Dataset.csv`: CSV file containing metadata corresponding to the audio, including gender, caste, region, speech rate, age group, and discipline group.

- `Final_Transcripts`: This folder contains transcripts corresponding to each audio. Each audio has three sets of transcripts:
  - `{Audio_ID}_manual`: Manually transcribed transcript.
  - `{Audio_ID}_auto`: YouTube automatic caption generated transcript.
  - `{Audio_ID}_whisper_base`: OpenAI Whisper generated transcript.

- `Final_Dataset_audios`: This folder contains all the audio files in the dataset.

## Usage

- To use this dataset, download the dataset from Google Drive using the above specified link. As the audio dataset 

- The `Final_Dataset.csv` file provides metadata for each audio in the dataset.

- The `Final_Transcripts` folder contains various transcripts associated with each audio.

## License

Attribution-ShareAlike 2.0 Generic (CC BY-SA 2.0) 

## Attribution

If you use this dataset in your research or projects, please cite this repository as follows:

[Provide citation information]

## Contact

For any inquiries, feedback, or collaboration opportunities, please contact [your-email@example.com].

---

[Add any additional information or acknowledgments here if needed.]

