# localizationkit

`localizationkit` is a toolkit for ensuring that your localized strings are the best that they can be.

Included are tests for various things such as:

* Checking that all strings have comments
* Checking that the comments don't just match the value
* Check that tokens have position specifiers
* Check that no invalid tokens are included

with lots more to come. 

## Getting started

### Configuration

To use the library, first off, create a configuration file that is in the TOML format. Here's an example:

```toml
default_language = "en"

[has_comments]
minimum_comment_length = 25
minimum_comment_words = 8

[token_matching]
allow_missing_defaults = true

[token_position_identifiers]
always = false
```

This configuration file sets that `en` is the default language (so this is the language that will be checked for comments, etc. and all tests will run relative to it). Then it sets various settings for each test. Every instance of `[something_here]` specifies that the following settings are for that test. For example, the test `has_comments` will now make sure that not only are there comments, but that they are at least 25 characters in length and 8 words in length. 

You can now load in your configuration:

```python
from localizationkit import Configuration

configuration = Configuration.from_file("/path/to/config.toml")
```

### Localization Collections

Now we need to prepare the strings that will go in. Here's how you can create an individual string:

```python
from localizationkit import LocalizedString

my_string = LocalizedString("My string's key", "My string's value", "My strings comment", "en")
```

This creates a single string with a key, value and comment, with its language code set to `en`. Once you've created some more (usually for different languages too), you can bundle them into a collection:

```python
from localizationkit import LocalizedCollection

collection = LocalizedCollection(list_of_my_strings)
```

### Running the tests

At this point, you are ready to run the tests:

```python
import localizationkit

results = localizationkit.run_tests(configuration, collection)

for result in results:
    if not result.succeeded():
        print("The following test failed:", result.name)
        print("Failures encountered:")
        for violation in result.violations:
            print(violation)
```

### Not running the tests

Some tests don't make sense for everyone. To skip a test you can add the following to your config file at the root:

```toml
blacklist = ["test_identifier_1", "test_identifier_2"]
```

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
