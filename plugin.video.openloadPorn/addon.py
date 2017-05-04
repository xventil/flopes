#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# por DeusMaior
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmc, xbmcaddon, HTMLParser

h = HTMLParser.HTMLParser()

addon_id = 'plugin.video.openloadPorn'
addon_version = '0.5.0'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'
base_url = 'http://openloadporn.com/'


##################################################

# MENUS############################################

def CATEGORIES():
    addDir('Latest Videos', 'http://openloadporn.com/index.html', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('pesquisa', 'url', 3, 'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addLink('', '', '', 0, '')
    addDir('21 Sextury', 'http://openloadporn.com/categories/21-sextury', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Asian Street Meat', 'http://openloadporn.com/categories/asian-street-meat', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Babes', 'http://openloadporn.com/categories/babes', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Blacked', 'http://openloadporn.com/categories/blacked', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Brazzers', 'http://openloadporn.com/categories/brazzers', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Bruno y Maria', 'http://openloadporn.com/categories/bruno-y-maria', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Busty Buffy', 'http://openloadporn.com/categories/busty-buffy', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Casting Couch X', 'http://openloadporn.com/categories/casting-couch-x', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('College Rules', 'http://openloadporn.com/categories/college-rules', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Dancing Bear', 'http://openloadporn.com/categories/Culioneros', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Dog Fart Network', 'http://openloadporn.com/categories/dog-fart-network', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Fake Agent', 'http://openloadporn.com/categories/fake-agent', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Fake Taxi', 'http://openloadporn.com/categories/fake-taxi', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Fakings', 'http://openloadporn.com/categories/fakings', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('HD Love', 'http://openloadporn.com/categories/hd-love', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('I Love the Beach', 'http://openloadporn.com/categories/i-love-the-beach', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Jim Slip', 'http://openloadporn.com/categories/jim-slip', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Legal Porno', 'http://openloadporn.com/categories/legal-porno', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('MMM 100', 'http://openloadporn.com/categories/mmm100', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Mofos', 'http://openloadporn.com/categories/mofos', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('NVAmateur', 'http://openloadporn.com/categories/nvamateur', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Naughty America', 'http://openloadporn.com/categories/naughty-america', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Passion HD', 'http://openloadporn.com/categories/passion-hd', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Porn Fidelity', 'http://openloadporn.com/categories/porn-fidelity', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Porn Pros', 'http://openloadporn.com/categories/porn-pros', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Private', 'http://openloadporn.com/categories/private', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Public Agent', 'http://openloadporn.com/categories/public-agent', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Pure Mature', 'http://openloadporn.com/categories/pure-mature', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Reality Kings', 'http://openloadporn.com/categories/reality-kings', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('RedDevilX', 'http://openloadporn.com/categories/reddevilx', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Sell Your GF', 'http://openloadporn.com/categories/sell-your-gf', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('SexMex', 'http://openloadporn.com/categories/sexmex', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Team Skeet', 'http://openloadporn.com/categories/team-skeet', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Woodman Casting', 'http://openloadporn.com/categories/woodman-casting', 1,
           'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    # addLink('', '', '', 0, '')
    addDir('openloadPorn Unofficial (Versão: ' + addon_version + ')', '', 0, '')
    xbmc.executebuiltin('Container.SetViewMode(%d)' % 100)


###################################################################################
# FUNCOES


def abrir_video(video):
    print "funcao abrir_video"
    try:
        xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
        xbmcPlayer.play(video)

    except:
        pass
        self.message("Erro ao abrir o video.")


def listar_filmes(url):
    codigo_fonte = abrir_url(url)
    match = re.compile('<div class="item">\s+<a href="(.+?)"\stitle="(.+?)"><img alt=".+?" src="(.+?)"').findall(
        codigo_fonte)
    for url, titulo, img in match:
        print url
        addDir(titulo, url, 2, img, False)
        xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
    match = re.compile("<a href='(.+?)' title='.+?'>&raquo").findall(codigo_fonte)
    for next_page in match:
        print next_page
        addDir('Proximo >>', 'http://openloadporn.com/' + next_page, 1, '')


def encontrar_fontes(url):
    codigo_fonte = abrir_url(url)
    match = re.compile('<div class="notice_reproductor"><iframe src="(.+?)"').findall(codigo_fonte)
    for ficheiro in match:
        cod_fonte = abrir_url(ficheiro)
        match = re.compile('src="(.+?)"').findall(cod_fonte)
        for link in match:
            import urlresolver
            stream_url = urlresolver.resolve(link)
            abrir_video(stream_url)


def pesquisa(url):
    kb = xbmc.Keyboard('', 'Search here')
    kb.doModal()
    if (kb.isConfirmed()):
        search = kb.getText()
        encode = urllib.quote(search)
        listar_filmes(base_url + 'search-' + str(encode) + '.html')
    else:
        CATEGORIES()


###################################################################################
# FUNCOES JÃ FEITAS


def abrir_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link


def addLink(name, url, iconimage, total, descricao):
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": descricao})
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz, totalItems=total)
    return ok


def addDir(name, url, mode, iconimage, pasta=True):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=pasta)
    return ok


############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass

try:
    iconimage = urllib.unquote_plus(params["iconimage"])
except:
    pass

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "Iconimage: " + str(iconimage)

###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode == None or url == None or len(url) < 1:
    #	print ""
    CATEGORIES()

elif mode == 1:
    print ""
    listar_filmes(url)

elif mode == 2:
    print ""
    encontrar_fontes(url)

elif mode == 3:
    print "modo3"
    pesquisa(base_url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))