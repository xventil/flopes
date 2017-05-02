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

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser
h = HTMLParser.HTMLParser()


addon_id = 'plugin.video.jizzman2'
addon_version = '0.4.0'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'



################################################## 

#MENUS############################################

def CATEGORIES():
    addDir('Latest Videos','http://jizzman2.com/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addLink('','','',0,'')
    addDir('Blacked','http://jizzman2.com/category/blacked/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Brazzers','http://jizzman2.com/category/brazzers-free-videos-hd/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Legal Porno','http://jizzman2.com/category/legalporno/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('BangBros','http://jizzman2.com/category/bangbros-free-videos-hd/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Reality Kings','http://jizzman2.com/category/realitykings/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Mofos','http://jizzman2.com/category/mofos/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Naughty America','http://jizzman2.com/category/naughtyamerica/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Digital Playground','http://jizzman2.com/category/digitalplayground/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    #addLink('', '', '', 0, '')
    addDir('Pesquisa','http://jizzman2.com/?s=')
    #addDir('Jizzman2 Unofficial (Versão: '+addon_version+')','',0,'')
    xbmc.executebuiltin('Container.SetViewMode(%d)' % 100)


###################################################################################
#FUNCOES


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
        match=re.compile('<a href="(.+?)">\s\s+<img width="520" height="293" src="(.+?)".+\s+<.a>\s+<.div>\s+<div class="item-head">\s+.+title="(.+?)"').findall(codigo_fonte)
        for url, img, titulo in match:
            print url
            addDir(titulo, url, 2, img, False)
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
        #match=re.compile('<a class="previouspostslink" rel="prev" href="(.+?)">').findall(codigo_fonte)
        #for prev_page in match:
        #    addLink('','','',0,'')
        #    addDir('Previous <<',prev_page,1,'')
        #match = re.compile('<a class="nextpostslink" rel="next" href="(.+?)">').findall(codigo_fonte)
        #for next_page in match:
        #    addLink('','','',0,'')
        #    addDir('Proximo >>',next_page,1,'')

def encontrar_fontes(url):
    codigo_fonte=abrir_url(url)
    match = re.compile('<iframe src="(.+?)"').findall(codigo_fonte)
    for ficheiro in match:
        cod_fonte = abrir_url(ficheiro)
        match = re.compile('<iframe src="(.+?)"').findall(cod_fonte)
        for link in match:
            import urlresolver
            stream_url = urlresolver.resolve(link)
            abrir_video(stream_url)

###################################################################################
#FUNCOES JÃ FEITAS


def abrir_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def addLink(name,url,iconimage,total,descricao):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', addonfolder + artfolder + 'fanart.png')
        liz.setInfo( type="Video", infoLabels={ "Title": name,  "Plot": descricao} )
        return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz, totalItems=total)
	return ok

def addDir(name,url,mode,iconimage,pasta=True):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta)
        return ok

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################
              
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

      
params=get_params()
url=None
name=None
mode=None
iconimage=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)




###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################


if mode==None or url==None or len(url)<1:
#	print ""
    CATEGORIES()

elif mode==1:
    print ""
    listar_filmes(url)

elif mode==2:
    print ""
    encontrar_fontes(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))