# Datasheet for dataset "TIE"

Questions from the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper, v7.

Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation

_The questions in this section are primarily intended to encourage dataset creators
to clearly articulate their reasons for creating the dataset and to promote transparency
about funding interests._

### For what purpose was the dataset created? 

The dataset was created to address the scarcity of technical domain data within the Indian context for the purpose of auditing and mitigating bias in State-of-the-Art Automatic Speech Recognition (ASR) systems.

### Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?
The videos of dataset has been sourced from [NPTEL channel of YouTube](https://www.youtube.com/nptelhrd) and annotated and curated by team of researchers ([Anand Kumar Rai](https://raianand1991.github.io/), [Siddharth D Jaiswal](https://sidd0602.github.io/) under supervision of Prof. [Animesh Mukherjee](https://cse.iitkgp.ac.in/~animeshm/) at IIT Kharagpur.


### Who funded the creation of the dataset? 

The creation of the dataset was not financially supported by any external funding.

### Any other comments?

## Composition

_Most of these questions are intended to provide dataset consumers with the
information they need to make informed decisions about using the dataset for
specific tasks. The answers to some of these questions reveal information
about compliance with the EU’s General Data Protection Regulation (GDPR) or
comparable regulations in other jurisdictions._

### What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?

The instances within the dataset represent technical lecture videos, encompassing 8740 hours of speech delivered by 332 Indian speakers across more than 20 varied lecture topics. Each video file has been enriched with annotations detailing demographic attributes such as teaching experience, gender, caste, and native region of the respective speaker, as well as audio metadata including speech rate, discipline, and lecture topic.The dataset also contains transcripts generated from YouTube and Whisper ASR for those lecture videos.

### How many instances are there in total (of each type, if appropriate)?

![Detailed Dataset Statistics](https://github.com/raianand1991/TIE/blob/main/Screenshot%202024-04-04%20145352.png)

### Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?

The dataset represents a sample of instances rather than encompassing all possible instances. The sample is not necessarily random but is rather curated to reflect certain demographics and characteristics, particularly those observed in higher educational institutes in India. Notably, there is a significant skew towards male speakers (approximately 95%) and those belonging to the unreserved caste category (approximately 73%), which mirrors the distribution observed in Indian higher education institutions. Additionally, there are insights into the representation of females in teaching positions and the distribution of lecturers belonging to reserved caste categories. The dataset also reflects the distribution of speakers based on teaching experience and native regions, with certain regions being underrepresented. Furthermore, annotations such as speech rate and discipline are provided for each lecture, which may result in an overlap of speakers across subcategories within the dataset.

### What data does each instance consist of? 

Each instance within the dataset consists of a technical lecture video delivered by an Indian speaker. Specifically, the data for each instance includes:

- Speech Content: The main content of the lecture delivered by the speaker.
- Speaker Information: Demographic attributes such as gender, teaching experience, caste, native region, and any other relevant information about the speaker.
- Audio Metadata: Information pertaining to the audio characteristics of the lecture, such as speech rate.
- Lecture Metadata: Details regarding the discipline and topic of the lecture.
- ASR Generated Transcripts: Transcripts corresponding to each lecture transcribed by YouTube ASR and OpenAI Whisper

### Is there a label or target associated with each instance?

The provided information doesn't explicitly mention a label or target associated with each instance. However, depending on the specific use case or analysis, it's possible that labels or targets could be derived or assigned based on the content or characteristics of the lectures. For example, if the dataset is used for speech recognition tasks, the target could be transcriptions of the speech content. If the dataset is used for demographic analysis, the target could be the demographic attributes of the speakers. If further annotation or labeling is required, it would typically be mentioned in the dataset documentation or specifications.

### Is any information missing from individual instances?

 The  TIE dataset includes comprehensive information for each individual instance.

### Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)?

Each instance represent an individual technical lecture delivered by a speaker, with associated metadata and annotations and no explicit relationships have been mentioned in the dataset.

### Are there recommended data splits (e.g., training, development/validation, testing)?

No

### Are there any errors, sources of noise, or redundancies in the dataset?

Firstly, the accuracy of manual transcripts may be compromised by human error during transcription. Additionally, self-annotated labels, such as gender and caste, pose challenges as they are not publicly available, making their determination difficult. Moreover, automatic identification of these attributes from names may introduce potential inaccuracies. Furthermore, the formal speech style and use of technical jargon in the videos may impact the performance of Automatic Speech Recognition (ASR) systems. Lectures involving live mathematical derivations or problem-solving, as opposed to those delivered using slides, may also influence ASR performance. Additionally, the non-deterministic outputs of ASR model components may lead to varying transcripts for the same video, further complicating analysis.

### Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?

_If it links to or relies on external resources, a) are there guarantees that they will
exist, and remain constant, over time; b) are there official archival versions of the
complete dataset (i.e., including the external resources as they existed at the time the
dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with
any of the external resources that might apply to a future user? Please provide descriptions
of all external resources and any restrictions associated with them, as well as links or other
access points, as appropriate._

### Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)?

_If so, please provide a description._

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

_If so, please describe why._

### Does the dataset relate to people? 

_If not, you may skip the remaining questions in this section._

### Does the dataset identify any subpopulations (e.g., by age, gender)?

_If so, please describe how these subpopulations are identified and provide a description of
their respective distributions within the dataset._

### Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?

_If so, please describe how._

### Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?

_If so, please provide a description._

### Any other comments?

## Collection process

_\[T\]he answers to questions here may provide information that allow others to
reconstruct the dataset without access to it._

### How was the data associated with each instance acquired?

_Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g.,
survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags,
model-based guesses for age or language)? If data was reported by subjects or indirectly
inferred/derived from other data, was the data validated/verified? If so, please describe how._

### What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?

_How were these mechanisms or procedures validated?_

### If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?

### Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?

### Over what timeframe was the data collected?

_Does this timeframe match the creation timeframe of the data associated with the instances (e.g.
recent crawl of old news articles)? If not, please describe the timeframe in which the data
associated with the instances was created._

### Were any ethical review processes conducted (e.g., by an institutional review board)?

_If so, please provide a description of these review processes, including the outcomes, as well as
a link or other access point to any supporting documentation._

### Does the dataset relate to people?

_If not, you may skip the remainder of the questions in this section._

### Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?

### Were the individuals in question notified about the data collection?

_If so, please describe (or show with screenshots or other information) how notice was provided,
and provide a link or other access point to, or otherwise reproduce, the exact language of the
notification itself._

### Did the individuals in question consent to the collection and use of their data?

_If so, please describe (or show with screenshots or other information) how consent was
requested and provided, and provide a link or other access point to, or otherwise reproduce, the
exact language to which the individuals consented._

### If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?

_If so, please provide a description, as well as a link or other access point to the mechanism
(if appropriate)._

### Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?

_If so, please provide a description of this analysis, including the outcomes, as well as a link
or other access point to any supporting documentation._

### Any other comments?

## Preprocessing/cleaning/labeling

_The questions in this section are intended to provide dataset consumers with the information
they need to determine whether the “raw” data has been processed in ways that are compatible
with their chosen tasks. For example, text that has been converted into a “bag-of-words” is
not suitable for tasks involving word order._

### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

_If so, please provide a description. If not, you may skip the remainder of the questions in
this section._

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

_If so, please provide a link or other access point to the “raw” data._

### Is the software used to preprocess/clean/label the instances available?

_If so, please provide a link or other access point._

### Any other comments?

## Uses

_These questions are intended to encourage dataset creators to reflect on the tasks
for which the dataset should and should not be used. By explicitly highlighting these tasks,
dataset creators can help dataset consumers to make informed decisions, thereby avoiding
potential risks or harms._

### Has the dataset been used for any tasks already?

_If so, please provide a description._

### Is there a repository that links to any or all papers or systems that use the dataset?

_If so, please provide a link or other access point._

### What (other) tasks could the dataset be used for?

### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

_For example, is there anything that a future user might need to know to avoid uses that
could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of
service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please
provide a description. Is there anything a future user could do to mitigate these undesirable
harms?_

### Are there tasks for which the dataset should not be used?

_If so, please provide a description._

### Any other comments?

## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? 

_If so, please provide a description._

### How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?

_Does the dataset have a digital object identifier (DOI)?_

### When will the dataset be distributed?

### Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

_If so, please describe this license and/or ToU, and provide a link or other access point to,
or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated
with these restrictions._

### Have any third parties imposed IP-based or other restrictions on the data associated with the instances?

_If so, please describe these restrictions, and provide a link or other access point to, or
otherwise reproduce, any relevant licensing terms, as well as any fees associated with these
restrictions._

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

_If so, please describe these restrictions, and provide a link or other access point to, or otherwise
reproduce, any supporting documentation._

### Any other comments?

## Maintenance

_These questions are intended to encourage dataset creators to plan for dataset maintenance
and communicate this plan with dataset consumers._

### Who is supporting/hosting/maintaining the dataset?

### How can the owner/curator/manager of the dataset be contacted (e.g., email address)?

### Is there an erratum?

_If so, please provide a link or other access point._

### Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?

_If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?_

### If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?

_If so, please describe these limits and explain how they will be enforced._

### Will older versions of the dataset continue to be supported/hosted/maintained?

_If so, please describe how. If not, please describe how its obsolescence will be communicated to users._

### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

_If so, please provide a description. Will these contributions be validated/verified? If so,
please describe how. If not, why not? Is there a process for communicating/distributing these
contributions to other users? If so, please provide a description._

### Any other comments?
