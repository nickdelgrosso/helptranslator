import sys
import pydoc
import googletrans

_original_output = pydoc.help._output

def set_help_lang(lang):
    if lang in googletrans.LANGUAGES:
        langcode = lang
    elif lang in googletrans.LANGCODES:
        langcode = googletrans.LANGCODES[lang]
    else:
        raise ValueError("'{}' not found in list of languages.  Available options are:\n{}".format(lang, googletrans.LANGUAGES))

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
