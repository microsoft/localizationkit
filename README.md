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

my_string = LocalizedString("My string's key", "My string's value", "My string's comment", "en")
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

# Rule documentation

Most tests have configurable rules. If a rule is not specified, it will use the default instead.

Some tests are opt in only. These will be marked as such.

## Comment Linebreaks

Identifier: `comment_linebreaks`
Opt-In: `true`

Checks that comments for strings do not contain linebreaks. Comments which contain linebreaks can interfere with parsing in other tools such as [dotstrings](https://github.com/microsoft/dotstrings).

## Comment Similarity

Identifier: `comment_similarity`

Checks the similarity between a comment and the string's value in the default language. This is achieved via `difflib`'s `SequenceMatcher`. More details can be found [here](https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher.ratio)

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `maximum_similarity_ratio` | float | Between 0 and 1 | 0.5 | Set the maximum similarity ratio between the comment and the string value. The higher the value, the more similar they are. The longer the string the more accurate this will be. |

</details>

## Duplicate Keys

Identifier: `duplicate_keys`

Checks that there are no duplicate keys in the collection.

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `all_languages` | boolean | `true` or `false` | `false` | Set to `true` to check that every language has unique keys, not just the default language. |

</details>

## Has Comments

Identifier: `has_comments`

Checks that strings have comments.

_Note: Only languages that have Latin style scripts are really supported for the words check due to splitting on spaces to check._

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `minimum_comment_length` | int | Any integer | 30 | Set the minimum allowable length for a comment. Set the value to negative to not check. |
| `minimum_comment_words` | int | Any integer | 10 | Set the minimum allowable number of words for a comment. Set the value to negative to not check. |

</details>

## Has Value

Identifier: `has_value`

Checks that strings have values. Since any value is enough for some strings, it simply makes sure that the string isn't None/null and isn't empty.

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `default_language_only` | boolean | `true` or `false` | `false` | Set to true to only check the default language for missing values. Otherwise all languages will be checked. |

</details>

## Invalid Tokens

Identifier: `invalid_tokens`

Checks that all format tokens in a string are valid.

_Note: This check is not language specific. It only works very broadly._

## Key Length

Identifier: `key_length`

Checks the length of the keys.

_Note: By default this test doesn't check anything. It needs to have parameters set to positive values to do anything._

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `minimum` | int | Any integer | -1 | Set the minimum allowable length for a key. Set the value to negative to not check. |
| `maximum` | int | Any integer | -1 | Set the maximum allowable length for a key. Set the value to negative to not check. |

</details>

## Objective-C Alternative Tokens

Identifier: `objectivec_alternative_tokens`
Opt-In: `true`

Checks that strings do not contain Objective-C style alternative position tokens.

Objective-C seems to be allows positional tokens of the form `%1@` rather than `%1$@`. While not illegal, it is preferred that all tokens between languages are consistent so that tools don't experience unexpected failures, etc.

## Swift Interpolation

Identifier: `swift_interpolation`
Opt-In: `true`

Checks that strings do not contain Swift style interpolation values since these cannot be localized.

## Token Matching

Identifier: `token_matching`

Checks that the tokens in a string match across all languages. e.g. If your English string is "Hello %s" but your French string is "Bonjour", this would flag that there is a missing token in the French string.

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `allow_missing_defaults` | boolean | `true` or `false` | `false` | Due to the way that automated localization works, usually there will be a default language, and then other translations will come in over time. If a translation is deleted, it isn't always deleted from all languages immediately. Setting this parameter to true will allow any strings in your non-default language to be ignored if that string is missing from your default language. |

</details>

## Token Position Identifiers

Identifier: `token_position_identifiers`

Check that each token has a position specifier with it. e.g. `%s` is not allowed, but `%1$s` is. Tokens can move around in different languages, so position specifiers are extremely important.

<details>
    <summary>Configuration</summary>

| Parameter | Type | Acceptable Values | Default | Details | 
| --- | --- | --- | --- | --- |
| `always` | boolean | `true` or `false` | `false` | If a string only has a single token, it doesn't need a position specifier. Set this to `true` to require it even in those cases.

</details>

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
