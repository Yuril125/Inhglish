#!/usr/bin/env python3

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import eng_to_ipa as ipa


def main() -> None:
    english = input("Enter English: ").split()
    transcription = [ipa.convert(word, keep_punct=False, retrieve_all=True) for word in english]
    print("\n".join(str(n) for n in transcription))


if __name__ == "__main__":
    while True:
        main()
