# ---------------------------------------------------------------------------
# Name: Create combo box and button
# Purpose: Make an interactive map
# Author: Keyur Kulkarni
# ---------------------------------------------------------------------------

import arcpy
import pythonaddins
arcpy.env.overwriteOutput = True


class ButtonClass1(object):
    """Implementation for Addin_Project_addin.button (Button)"""
    def __init__(self):
        self.enabled = False
        self.checked = False

    def onClick(self):
        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        layers = arcpy.mapping.ListLayers(self.mxd)
        # Turn on the US and Selected layer, turn off the rest
        for layer in layers:
            if layer.name == fc.name or layer.name == "UnitedStates":
                layer.visible = True
            else:
                layer.visible = False

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        count = int(str(arcpy.GetCount_management(fc.dataSource)))
        # new_count = count / 2
        # Print number of tweets for selected layer
        pythonaddins.MessageBox("Total tweet mentions {:0}".format(count),
                                "Total Mentions")


class ComboBoxClass2(object):
    """Implementation for Addin_Project_addin.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = '0123456789012345'
        self.width = '0123456789012345'

        self.mxd = arcpy.mapping.MapDocument("CURRENT")
        layers = arcpy.mapping.ListLayers(self.mxd)
        self.items = []
        # Do not show US shapefile in combo list
        for layer in layers:
            if layer.name == "UnitedStates":
                layer.visible = True
            else:
                layer.visible = False
                self.items.append(layer.name)

        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

    def onSelChange(self, selection):
        print "New selection : ", selection
        layer = arcpy.mapping.ListLayers(self.mxd, selection)[0]
        global fc
        fc = layer
        button.enabled = True
        fc.visible = False
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        pass

    def onEnter(self):
        pass

    def refresh(self):
        pass
