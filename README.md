<p align="center">
    <img src="doc/logo.svg" height="200px" alt="logo" title="Answerable">
</p>
<h1 align="center">Answerable</h1>
<h3 align="center">Stack Overflow unanswered questions recommendation system</h3>
<p align="center">
	<a href="LICENSE">
        <img alt="license" src="https://img.shields.io/badge/license-MIT-informational">
    </a>
	<img alt="repo-size" src="https://img.shields.io/github/repo-size/MiguelMJ/Answerable">
	<img alt="python3.8" src="https://img.shields.io/badge/python-3.8-informational">
	<a href="https://github.com/MiguelMJ/Answerable/wiki">
        <img alt="documentation" src="https://img.shields.io/badge/documentation-wiki-success">
    </a>
	<a href="https://github.com/psf/black">
        <img alt="code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>


Answerable is a Python program that learns from your answers in Stack Overflow and use them to recommend you questions that you could answer.

___This project is still under development.___ [![last commit](https://img.shields.io/github/last-commit/MiguelMJ/Answerable)](https://github.com/MiguelMJ/Answerable)

**Preview**

<p align="center"><img src="doc/preview.png" alt="preview"></p>

**Table of contents**

<span id="toc"></span>

  - [Quick guide](#Quick-guide32)
  - [Contributors](#Contributors62)
  - [To do](#To-do68)
  - [Contributing](#Contributing86)
  - [License](#License95)

<h2 id="Quick-guide32">Quick guide</h2> 

[[TOC](#toc)]

- Clone the repository

    ```bash
    git clone https://github.com/MiguelMJ/Answerable.git
    ```

- Save the user (see [how to get your relevant user information](https://github.com/MiguelMJ/Answerable/wiki/Getting_user_info))

    ```bash
    python answerable.py save -u ID [-t FILE]
    ```

- Get information of your profile

    ```bash
    python answerable.py summary -u ID
    ```

- Get recommendations

  ```bash
  python answerable.py recommend -u ID
  ```

_To see a more complete guide, visit the [wiki](https://github.com/MiguelMJ/Answerable/wiki)._

<h2 id="Contributors62">Contributors</h2> 

[[TOC](#toc)]

Be the first on this list!

<h2 id="To-do68">To do</h2> 

[[TOC](#toc)]

- [x] Test all documented behaviour (argument usage).
- [ ] Adapt behaviour for users with authentication token.
- [x] Limit the number of answers retrieved from users with too many answers.
  - Too many answers reduce the recommendation quality.
  - Too many answers drastically increases the retrieval time.

**Low priority**

- [ ] Include the rest of the Stack Exchange communitites.
- [ ] Make a GUI.
- [ ] Add flexible filters (Don't show questions with negative score e.g).
- [ ] Display statistics about the information taken into account to make the recommendations.
- [ ] Try out more learning models and integrate them.

<h2 id="Contributing86">Contributing</h2> 

[[TOC](#toc)]

- In addition to the tasks listed above, you can also contribute by testing the program yourself and reporting any issue[![](https://img.shields.io/github/issues/MiguelMJ/Answerable?style=social)](https://github.com/MiguelMJ/Answerable/issues).
- Give this project some visibility:
  - :star: Star this repository [![](https://img.shields.io/github/stars/MiguelMJ/Answerable?style=social)](https://github.com/MiguelMJ/Answerable/stargazers).
  - :arrow_up: Upvote it in [Stack Apps](https://stackapps.com/questions/8805/placeholder-answerable-a-recomendator-of-unanswered-questions).

<h2 id="License95">License</h2> 

[[TOC](#toc)]

Answerable uses the MIT license, a copy of which you can find [here](LICENSE), in the repo.


```

```
