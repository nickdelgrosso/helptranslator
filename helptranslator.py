import sys
import pydoc
import itertools
import googletrans
import json

_original_output = pydoc.help._output

def set_help_lang(language):
    """Overrides the help() function output to a given language, using Google Translate."""
    if language in googletrans.LANGUAGES:
        langcode = language
    elif language in googletrans.LANGCODES:
        langcode = googletrans.LANGCODES[language]
    else:
        raise ValueError("'{}' not found in list of languages.  Available options are:\n{}".format(language, googletrans.LANGUAGES))

    if langcode == 'en':
        pydoc.help._output = _original_output
        return

    class STDOutTrans(object):
        def write(self, string):
            translator = googletrans.Translator()
            translated = translator.translate(string, dest=langcode)
            sys.stdout.write(translated.text)

    pydoc.help._output = STDOutTrans()
    return


def parse_module_doc(module):
    """Returns a dict containing all the help text in a module."""
    docs = {'module': module.__name__}
    for fun in itertools.chain([module], module.__dict__):
        if hasattr(fun, '__doc__'):
            docs[str(fun)] = fun.__doc__
    return docs


def translate_langdict(langdict, lang):
    """calls Google translate on all values in a dict, returning a translated dict."""
    translated_dict = {'module': langdict['module']}
    for fun, string in langdict.items():
        translator = googletrans.Translator()
        translated = translator.translate(string, dest=lang)
        translated_dict[fun] = translated.text
    return translated_dict


def write_lang_stubfile(langdict):
    """Writes the translations from a langdict to file."""
    with open(langdict['module'] + '.doclang', 'w') as f:
        json.dump(langdict, f)


def read_lang_stubfile(fname):
    """Returns a dict from a '.doclang' file name"""
    with open(fname) as f:
        return json.load(f)
