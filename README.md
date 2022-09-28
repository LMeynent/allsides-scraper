![Allsides logo](https://www.allsides.com/sites/all/themes/allsides/images/AllSides-Logo.svg)

# Allsides scraper

In this repository, we propose a tool and ready-to-use dataset from the [Allsides](https://www.allsides.com/media-bias/ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B%5D=1&field_news_source_type_tid%5B%5D=2&field_news_source_type_tid%5B%5D=3&field_news_source_type_tid%5B%5D=4&field_news_source_type_tid%5B%5D=5&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title=) website, which rates the political bias of news sources.

## How it works

We manually get the HTML page with fully scrolled-down ratings, for all different categories. These were collected on September 28th 2022. We then use a web scraper to gather additional information and store the data in a tabular format.

## Usage

We provide an `environment.yml` file to use with [`conda`](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). To run the script:

```
conda env create -f environment.yml
conda activate allsides-scraper
python allsides-scraper.py
```

## Methodology

The bias rating methodology of Allsides is available [here](https://www.allsides.com/media-bias/media-bias-rating-methods).

## License

The Allsides data is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/). These ratings may be used for research or noncommercial purposes with attribution. The use of the present repository is therefore subject to the respect of this license's terms.
