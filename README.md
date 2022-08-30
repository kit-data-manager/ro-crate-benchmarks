# Benchmarks for RO-Crate libraries
This repository contains benchmarks to compare the performance of different RO-Crate libraries. Nikola Tzotchev created them for his bachelor thesis *A Software Library for Research Data Packaging and Exchange*.

## Setting up and running the benchmarks

As the benchmarks compares different libraries from different programming ecosystems, the setup is a bit diverse.

- The pyproject.toml can, for example be used with [poetry](https://python-poetry.org/docs/master/basic-usage/) to set up an virtual environment with all required dependencies, the correct python version and its jupyter kernel, etc.
    - `poetry install` in this folder will set everything up.
    - `poetry shell` will give you access to the installed environment. Start your Jupyter Lab (or vscode) here in this shell.
    - ro-crate-py will also be automatically installed in this environment.
- ro-crate-java needs to be cloned using git and stored locally. In the Jupyter-Notebooks, which will run the tests, you need to adjust the variable `java_library_location` to contain the path to ro-crate-java on the local device. To make the Crate-Previews work, run `npm install -g ro-crate-html-js`.
- ro-crate-ruby needs to be installed with gem: `gem install ro-crate`
- ro-crate-py will also be benchmarked using the optimized [pypy interpreter](https://www.pypy.org/). While it can be [installed from the webpage](https://www.pypy.org/download.html), you may consider using a package manager of your operating system. On macOS, the easiest way to install it is using [homebrew](https://brew.sh/): `brew install pypy3`. Installing ro-crate-py for pypy3 canbe done using these steps:
    - `pypy3 -m ensurepip`
    - `pypy3 -m pip install -U pip wheel`
    - `pypy3 -m pip install -U rocrate`
- Before running any tests, run the [file that generates the data entities](generate_data.py): `python3 generate_data.py`

The results can be viewed in Nikola's thesis (may use older versions). More up-to-date runs can be seen by opening the notebooks. The results are stored inside. Each notebook corresponds to one of the tests described below. To run them, execute the Notebook from the first to the last cell.

## 1. single crate performance

These are done in the jupyter notebook named [single_crate_plot](single_crate_plot.ipynb)

There were 5 different benchmarks done here:
- contextual entities:

Here, a different amount of contextual entities is added to a single crate and the time is measured.
The crates look like this:
```
{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "./",
            "@type": "Dataset",
            "datePublished": "2022-05-03T11:40:05+00:00"
        },
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        {
            "@id": "https://www.example.com/0",
            "@type": "Person",{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "./",
            "@type": "Dataset",
            "datePublished": "2022-05-03T11:51:41+00:00",
            "hasPart": [
                {
                    "@id": "file0"
                },
                {
                    "@id": "file1"
                }
            ]
        },
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        {
            "@id": "file0",
            "@type": "File",
            "author": {
                "@id": "#id0"
            }
        },
        {
            "@id": "#id0",
            "@type": "Person",
            "name": "Joe Bloggs"
        },
            "name": "Joe Bloggs"
        },
        {
            "@id": "https://www.example.com/1",
            "@type": "Person",
            "name": "Joe Bloggs"
        }, ........
```

- data entities remote:

Here, only remote data entities are added.
The crate looks like this:

```

{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "./",
            "@type": "Dataset",
            "datePublished": "2022-05-03T11:45:33+00:00",
            "hasPart": [
                {
                    "@id": "https://www.example.com/0"
                },
                {
                    "@id": "https://www.example.com/1"
                }
            ]
        },
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        {
            "@id": "https://www.example.com/0",
            "@type": "File"
        },
        {
            "@id": "https://www.example.com/1",
            "@type": "File"
        }
    ]
}⏎                                                                        

```
- data entities local:

Looks the same as the above one, but the entities used are locally present, generated by this [file](generate_data.py)
- mixture:

Adds the same amount of local data entities and person entities, each data entity then has as author one of the person entities.

```
{
    "@context": "https://w3id.org/ro/crate/1.1/context",
    "@graph": [
        {
            "@id": "./",
            "@type": "Dataset",
            "datePublished": "2022-05-03T11:51:41+00:00",
            "hasPart": [
                {
                    "@id": "file0"
                },
                {
                    "@id": "file1"
                }
            ]
        },
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        {
            "@id": "file0",
            "@type": "File",
            "author": {
                "@id": "#id0"
            }
        },
        {
            "@id": "#id0",
            "@type": "Person",
            "name": "Joe Bloggs"
        },................
    ]
}
```
- mixture with deletion:

The same as the above, but then the entities are deleted starting with the person ones and ending with the data entities.

## 2. multiple crate performance

Here the amount of crates created varies, the entities inside a single crate are the same as the ones in the single crate mixture benchmark.
The benchmark is done in [this notebook](multiple_crates.ipynb)


## 3. read and write

Very similar to the previos test but the crates are written and then read (every single one of them).
This benchmark is done in [this notebook](read_write.ipynb)

