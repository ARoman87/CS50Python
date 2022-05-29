import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "iframe" in s:
        try:
            url = re.findall(
                "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                s,
            )
            new_url = url[0]
            if "youtube" in new_url:
                if "https://www.youtube.com/embed" in new_url:
                    newnew = new_url.replace(
                        "https://www.youtube.com/embed", "https://youtu.be"
                    )
                    return newnew
                elif "http://youtube.com/embed" in new_url:
                    newnew = new_url.replace(
                        "http://youtube.com/embed", "https://youtu.be"
                    )
                    return newnew
                elif "https://youtube.com/embed" in new_url:
                    newnew = new_url.replace(
                        "https://youtube.com/embed", "https://youtu.be"
                    )
                    return newnew

        except:
            None


if __name__ == "__main__":
    main()
