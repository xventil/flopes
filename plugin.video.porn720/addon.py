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


addon_id = 'plugin.video.porn720'
addon_version = '0.4.0'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'


################################################## 

#MENUS############################################

def CATEGORIES():
    addDir('Latest Videos','http://porn720.net/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addLink('','','',0,'')
    addDir('2 girls and a guy','http://porn720.net/tag/2-devki-i-paren',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('2 guys and a girl','http://porn720.net/tag/2-parnya-i-devushka',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Anal sex','http://porn720.net/tag/analnyiy-seks',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Blondes','http://porn720.net/tag/blondinki',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Huge Loads','http://porn720.net/tag/bolshie-siski',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Brunettes','http://porn720.net/tag/bryunetki',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Parties','http://porn720.net/tag/vecherinki-i-pati',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('The maids','http://porn720.net/tag/gornichnyie-domohozyayki',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Stockings','http://porn720.net/tag/devochki-v-chulkah',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Makes the guy','http://porn720.net/tag/drochit-parnyu',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Casting','http://porn720.net/tag/kastingi',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Cum Inside','http://porn720.net/tag/konchayut-vnutr',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Cumshot','http://porn720.net/tag/konchil-na-litso',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Beautiful porn','http://porn720.net/tag/krasivoe-porno',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Cooney, licks pussy','http://porn720.net/tag/kuni',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Footwear','http://porn720.net/tag/latino',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Licking the ass','http://porn720.net/tag/lizhet-popu',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Massages','http://porn720.net/tag/massazhi',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Blowjob, Fuck in the mouth','http://porn720.net/tag/oralnyiy',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('On heels','http://porn720.net/tag/na-kablukah',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('In the kitchen','http://porn720.net/tag/na-kuhne',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Outdoors','http://porn720.net/tag/na-prirode',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Black','http://porn720.net/tag/negryi-i-mulatki',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('New Year Eve','http://porn720.net/tag/novogodnee',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('POV','http://porn720.net/tag/ot-pervogo-litsa',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Peeping','http://porn720.net/tag/podglyadyivaniya',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Just Sex','http://porn720.net/tag/prosto-seks',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Redheads','http://porn720.net/tag/ryizhie',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Sex in the car','http://porn720.net/tag/v-mashine',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Sex at work, in the office','http://porn720.net/tag/seks-na-rabote',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Bbw','http://porn720.net/tag/tolstushki',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Uniform','http://porn720.net/tag/uniforma',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Halloween','http://porn720.net/tag/halloween',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addLink('','','',0,'')
    addDir('720Porn Unofficial (Versão: '+addon_version+')','',0,'')


###################################################################################
#FUNCOES


def abrir_video(video,subtitle):
     print "funcao abrir_video"
     try:
         xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
         xbmcPlayer.play(video)
         xbmc.Player().setSubtitles(subtitle)         
		 
     except:
         pass
         self.message("Erro ao abrir o video.")

def listar_filmes(url):
        codigo_fonte = abrir_url(url)
        match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img width="240" height="180" src="(.+?)"').findall(codigo_fonte)
        for url,titulo,img in match:
            print url +" "+ titulo +" "+ img 
            addDir(titulo,url,2, img,False)
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
        #match=re.compile('<a class="previouspostslink" rel="prev" href="(.+?)">').findall(codigo_fonte)
        #for prev_page in match:
        #    addLink('','','',0,'')
        #    addDir('Previous <<',prev_page,1,'')
        match = re.compile('<a class="nextpostslink" rel="next" href="(.+?)">').findall(codigo_fonte)
        for next_page in match:
            addLink('','','',0,'')
            addDir('Proximo >>',next_page,1,'')

def encontrar_fontes(url):
    codigo_fonte=abrir_url(url)
    match = re.compile('"720p":"(.+?)"}};').findall(codigo_fonte)
    for ficheiro in match:
        legenda = ''
        abrir_video(ficheiro,legenda)
	
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