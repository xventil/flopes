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


addon_id = 'plugin.video.porn720com'
addon_version = '0.4.0'
selfAddon = xbmcaddon.Addon(id=addon_id)
addonfolder = selfAddon.getAddonInfo('path')
artfolder = '/resources/img/'



################################################## 

#MENUS############################################

def CATEGORIES():
    addDir('Latest Videos','http://porn720.com/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addLink('','','',0,'')
    addDir('Anal Sex','http://porn720.com/category/anal/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Asian','http://porn720.com/category/asian/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('In Office','http://porn720.com/category/at-work/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Big Ass','http://porn720.com/category/big-ass/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Big Dick','http://porn720.com/category/big-dick',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Big Tits','http://porn720.com/category/big-tits/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Ebony','http://porn720.com/category/ebony/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Blonde','http://porn720.com/category/blonde/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Blowjob','http://porn720.com/category/blowjob/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Brunette','http://porn720.com/category/brunette/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Casting','http://porn720.com/category/casting/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Cream Pie','http://porn720.com/category/cream-pie/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Cuckold','http://porn720.com/category/cuckold/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Deep Throats','http://porn720.com/category/deep-throats/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Doctor/Nurse','http://porn720.com/category/doctor-nurse/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Double Penetration','http://porn720.com/category/double-penetration/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Facial','http://porn720.com/category/facial/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('POV','http://porn720.com/category/first-person/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Fisting','http://porn720.com/category/fisting/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Foursome','http://porn720.com/category/foursome/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('GangBang','http://porn720.com/category/gangbang/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Group Sex','http://porn720.com/category/group-sex/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Hardcore Sex','http://porn720.com/category/hardcore/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('In School','http://porn720.com/category/in-school/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('In Sports','http://porn720.com/category/in-sports/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Interracial','http://porn720.com/category/interracial/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Latina','http://porn720.com/category/latina/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Lesbian','http://porn720.com/category/lesbian/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Massage','http://porn720.com/category/massage/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('MILFs','http://porn720.com/category/milfs/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Moms','http://porn720.com/category/moms/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Natural Tits','http://porn720.com/category/natural-tits/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Old+Young','http://porn720.com/category/oldyoung/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Outdoor','http://porn720.com/category/outdoor/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Parody','http://porn720.com/category/parody/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Public Pickup','http://porn720.com/category/public-pickup/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Public Sex','http://porn720.com/category/public-sex/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Red Head','http://porn720.com/category/red-head/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Russian','http://porn720.com/category/russian/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Sex Party','http://porn720.com/category/sex-party/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Sex Toys','http://porn720.com/category/sex-toys/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Solo Girls','http://porn720.com/category/solo-girls/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Stockings','http://porn720.com/category/stockings/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Tattoo','http://porn720.com/category/tattoo/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Teens','http://porn720.com/category/teens/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Threesome','http://porn720.com/category/threesome/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('Uniform','http://porn720.com/category/uniform/',1,'http://www.ckfilms.com/wp-content/uploads/2013/09/clapper.png')
    addDir('720Porn.com Unofficial (Versão: '+addon_version+')','',0,'')


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
        match=re.compile('<div class="thumb2">\s*<a class="photo" href="(.+?)">\s*<div class="photo-bg"><span class="icons icon-photo-hover"><.span><.div>\s*<img .+" .>\s*<!--..<img src="(.+?)" class="preview"\s*alt="" width="180" height="140" .>.+\s*.+\s*.+\s*.+\s*.+\s*.+\s*.+\s*.+\s*.+\s*<div class="title"><a href=".+?" title="(.+?)"').findall(codigo_fonte)
        for url,img,titulo in match:
            print url +" "+ titulo +" "+ img 
            addDir(titulo,url,2, img,False)
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
        match=re.compile('<a class="previouspostslink" rel="prev" href="(.+?)">').findall(codigo_fonte)
        for prev_page in match:
        #    addLink('','','',0,'')
            addDir('Previous <<',prev_page,1,'')
        match = re.compile('<a class="nextpostslink" rel="next" href="(.+?)">').findall(codigo_fonte)
        for next_page in match:
        #    addLink('','','',0,'')
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