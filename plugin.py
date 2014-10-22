from Plugins.Plugin import PluginDescriptor
from Screens.Console import Console

cmd = "/usr/lib/enigma2/python/Plugins/Extensions/BackupLB/backup.sh /hdd"

def main(session, **kwargs):
    	session.open(Console,_("BACKUP-LB"),[cmd])

def menu(menuid, **kwargs):
	if menuid == "mainmenu":
		return [(_("BACKUP-LB"), main, _("Backup para Gigablue"), 48)]
	return []

   	
def Plugins(**kwargs):
    	return [PluginDescriptor(name="BACKUP-LB", description=_("Backup en HDD imagen gigablue"), where = [PluginDescriptor.WHERE_PLUGINMENU], fnc=main, icon="backup.png"),
		PluginDescriptor(name=_("BACKUP-LB"), description=_("Backup en HDD imagen gigablue"), where = [PluginDescriptor.WHERE_MENU], fnc=menu),
            	PluginDescriptor(name="BACKUP-LB", description=_("Backup en HDD imagen gigablue"), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=main)]
