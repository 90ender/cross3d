##
#	\namespace	blur3d.api.abstract.abstractsceneobjectgroup
#
#	\remarks	The AbstractSceneObjectGroup class provides an interface for working on sets of SceneObject's as a singular group
#	
#	\author		eric@blur.com
#	\author		Blur Studio
#	\date		09/08/10
#

class AbstractSceneObjectGroup:
	def __eq__( self, other ):
		"""
			\remarks	determines whether one 3dObject instance is equal to another by comparing the pointers to their native object pointers
			\param		other	<variant>
			\return		<bool> success
		"""
		if ( isinstance( other, AbstractSceneObjectGroup ) ):
			return self._nativePointer == other._nativePointer
		return False
		
	def __init__( self, scene, nativeGroup ):
		# define custom properties
		self._scene					= scene
		self._nativePointer			= nativeGroup
		self._materialOverride		= None			# blur3d.api.SceneMaterial 					- material to be used as the override material for the objects in this group
		self._materialOverrideFlags	= 0				# blur3d.constants.MaterialOverrideOptions		- options to be used when overriding materials
		self._propSetOverride		= None			# blur3d.api.SceneObjectPropSet				- property set to be used as the override properties for the objects in this group
		
	#------------------------------------------------------------------------------------------------------------------------
	# 												protected methods
	#------------------------------------------------------------------------------------------------------------------------
	def _addNativeObjects( self, nativeObjects ):
		"""
			\remarks	[abstract]	add the native objects to the object group
			\sa			addObjects, addSelection
			\param		nativeObjects	<list> [ <variant> nativeObject, .. ]
			\return		<bool> success
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def _clearNativeObjects( self ):
		"""
			\remarks	[abstract] clear the native objects from this group
			\sa			clearObjects
			\return		<bool> success
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def _clearNativeMaterialOverride( self ):
		"""
			\remarks	[virtual] clear the native objects of any material overrides for this group
			\sa			blur3d.api.Scene._clearNativeMaterialOverride
			\return		<bool> success
		"""
		return self._scene._clearNativeMaterialOverride( self._nativeObjects() )
	
	def _clearNativePropSetOverride( self ):
		"""
			\remarks	[virtual] clear the native objects of any property set overrides for this group
			\sa			blur3d.api.Scene._clearNativePropSetOverride
			\return		<bool> success
		"""
		return self._scene._clearNativePropSetOverride( self._nativeObjects() )
	
	def _nativeObjects( self ):
		"""
			\remarks	[abstract] return a list of the native objects that are currently on this group
			\sa			objects
			\return		<list> [ <variant> nativeObject, .. ]
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return []
	
	def _nativeMaterialOverride( self ):
		"""
			\remarks	[abstract] return the current override material for this object group
			\return		<variant> nativeMaterial || None
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return None
	
	def _setNativeMaterialOverride( self, nativeMaterial, options = -1 ):
		"""
			\remarks	[virtual] set the current override materials for this object group
			\sa			blur3d.api.Scene._setNativeMaterialOverride
			\param		<variant> nativeMaterial || None
			\return		<bool> success
		"""
		if ( options == -1 ):
			options = self.materialOverrideFlags()
			
		return self._scene._setNativeMaterialOverride( self._nativeObjects(), nativeMaterial, options = options )
	
	def _setNativePropSetOverride( self, nativePropSet ):
		"""
			\remarks	[virtual] set the current override property set for this object group
			\sa			blur3d.api.Scene._setNativePropSetOverride
			\param		<variant> nativePropSet || None
			\return		<bool> success
		"""
		return self._scene._setNativePropSetOverride( self._nativeObjects(), nativePropSet )
	
	#------------------------------------------------------------------------------------------------------------------------
	# 												public methods
	#------------------------------------------------------------------------------------------------------------------------
	def addObjects( self, objects ):
		"""
			\remarks	add the objects to this layer
			\sa			addSelection, _addNativeObjects
			\param		objects		<list> [ <blur3d.api.SceneObject>, .. ]
			\return		<bool> success
		"""
		return self._addNativeObjects( [ object.nativePointer() for object in objects ] )
	
	def addSelection( self ):
		"""
			\remarks	add the selected scene objects to this layer
			\sa			addObjects, _addNativeObjects
			\return		<bool> success
		"""
		return self._addNativeObjects( self._scene._nativeSelection() )
	
	def clearMaterialOverride( self ):
		"""
			\remarks	clears the current material overrides from this object group's objects
			\return		<bool> success
		"""
		return self._clearNativeMaterialOverride()
	
	def clearMaterialOverrideFlags( self ):
		"""
			\remarks	return whether or not the inputed flag is set in the override options
			\sa			hasMaterialOverrideFlag, materialOverrideFlags, setMaterialOverrideFlag, setMaterialOverrideFlags
			\return		<bool> success
		"""
		self._materialOverrideFlags = 0
		return True
	
	def clearPropSetOverride( self ):
		"""
			\remarks	clears the current prop set override from this object group's objects
			\return		<bool> success
		"""
		return self._clearNativePropSetOverride()
	
	def deselect( self ):
		"""
			\remarks	deselects the objects on this layer from the scene
			\sa			select, setSelected
			\return		<bool> success
		"""
		return self.setSelected(False)
	
	def freeze( self ):
		"""
			\remarks	freezes (locks) the objects on this layer in the scene
			\sa			setFrozen, unfreeze
			\return		<bool> success
		"""
		return self.setFrozen(True)
	
	def hasMaterialOverrideFlag( self, flag ):
		"""
			\remarks	return whether or not the inputed flag is set in the override options
			\sa			clearMaterialOverrideFlags, materialOverrideFlags, setMaterialOverrideFlag, setMaterialOverrideFlags
			\param		flag	<blur3d.constants.MaterialOverrideOptions>
			\return		<bool> exists
		"""
		return (self._materialOverrideFlags & flag) != 0
	
	def hide( self ):
		"""
			\remarks	hides the objects on this layer in the scene
			\sa			setHidden, unhide
			\return		<bool> success
		"""
		return self.setHidden( True )
	
	def isEmpty( self ):
		"""
			\remarks	returns whether or not this layer is empty (contains no chidren)
			\sa			_nativeObjects
			\return		<bool> empty
		"""
		return len( self._nativeObjects() ) == 0
	
	def isFrozen( self ):
		"""
			\remarks	[abstract] retrieve the group name for this object group instance
			\return		<bool> frozen
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
		
	def isHidden( self ):
		"""
			\remarks	[abstract] retrieve the group name for this object group instance
			\return		<bool> hidden
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def isolate( self ):
		"""
			\remarks	isolates the objects in this group in the scene
			\sa			AbstractScene._isolateNativeObjects
			\return		<bool> success
		"""
		return self._scene._isolateNativeObjects( self._nativeObjects() )
	
	def groupName( self ):
		"""
			\remarks	[abstract] retrieve the group name for this object group instance
			\return		<str> name
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return ''
	
	def nativePointer( self ):
		"""
			\remarks	return the pointer to the native object that is wrapped
			\return		<variant> nativeLayer
		"""
		return self._nativePointer
	
	def objects( self ):
		"""
			\remarks	returns the SceneObject's that are associated with this layer
			\return		<list> [ <blur3d.api.SceneObject>, .. ]
		"""
		from blur3d.api import SceneObject
		return [ SceneObject( self._scene, obj ) for obj in self._nativeObjects() ]
	
	def materialOverride( self ):
		"""
			\remarks	return the current override material for this object set
			\return		<blur3d.api.SceneMaterial> || None
		"""
		nativeMaterial = self._nativeMaterialOverride()
		if ( nativeMaterial ):
			from blur3d.api import SceneMaterial
			return SceneMaterial( self.scene(), nativeMaterial )
		return None
	
	def materialOverrideFlags( self ):
		"""
			\remarks	return the duplication flags for the override material
			\sa			clearMaterialOverrideFlags, hasMaterialOverrideFlag, setMaterialOverrideFlag, setMaterialOverrideFlags
			\return		<blur3d.constants.MaterialOverrideOptions>
		"""
		return self._materialOverrideFlags
	
	def propSetOverride( self ):
		"""
			\remarks	return the current override prop set for this object set
			\return		<blur3d.api.SceneObjectPropSet> || None
		"""
		return self._propSetOverride
	
	def remove( self, removeObjects = False ):
		"""
			\remarks	[abstract] remove the layer from the scene (objects included when desired)
			\param		removeObjects	<bool>	when true, the objects on the layer should be removed from the scene, otherwise
												only the layer should be removed
			\return		<bool> success
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def scene( self ):
		"""
			\remarks	return the scene instance that this layer is a member of
			\return		<blur3d.api.Scene>
		"""
		return self._scene
	
	def select( self ):
		"""
			\remarks	selects the items on this layer
			\sa			deselect, setSelected
			\return		<bool> success
		"""
		return self.setSelected(True)
	
	def setActive( self, state ):
		"""
			\remarks	[abstract] mark this layer as the active scene layer
			\sa			isActive
			\param		state	<bool>
			\return		<bool> success
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def setMaterialOverride( self, material, options = -1 ):
		"""
			\remarks	set the override material on the objects for this set
			\sa			_setNativeMaterialOverride
			\param		material	<blur3d.api.SceneMaterial> || None
			\param		options		<blur3d.constants.MaterialOverrideOptions>
			\return		<bool> success
		"""
		nativeMaterial = None
		if ( material ):
			nativeMaterial = material.nativePointer()
		
		if ( options == -1 ):
			options = self.materialOverrideFlags()
			
		return self._setNativeMaterialOverride( nativeMaterial, options = options )
		
	def setMaterialOverrideFlag( self, flag, state = True ):
		"""
			\remarks	set the inputed flag on or off based on the state
			\sa			clearMaterialOverrideFlags, hasMaterialOverrideFlag, materialOverrideFlags, setMaterialOverrideFlags
			\param		flag	<blur3d.constants.MaterialOverrideOptions>
			\param		state	<bool>
			\return		<bool> success
		"""
		if ( state ):
			self._materialOverrideFlags |= flag
		else:
			self._materialOverrideFlags ^= flag
		return True
	
	def setMaterialOverrideFlags( self, flags ):
		"""
			\remarks	set all of the duplication flags for override materials
			\sa			clearMaterialOverrideFlags, hasMaterialOverrideFlag, materialOverrideFlags, setMaterialOverrideFlag
			\param		flags	<blur3d.constants.MaterialOverrideOptions>
			\return		<bool> success
		"""
		self._materialOverrideFlags = flags
		return True
	
	def setPropSetOverride( self, propSet ):
		"""
			\remarks	set the override properties on the objects that are a part of this object group
			\param		propSet		<blur3d.api.SceneObjectPropSet>
			\return		<bool> success
		"""
		return self._setNativePropSetOverride( propSet.nativePointer() )
	
	def setFrozen( self, state ):
		"""
			\remarks	set the frozen (locked) state for the objects on this layer
			\sa			freeze, unfreeze, _nativeObjects, blur3d.api.Scene._freezeNativeObjects
			\param		state	<bool>
			\return		<bool> success
		"""
		return self._scene._freezeNativeObjects( self._nativeObjects(), state )
	
	def setGroupName( self, groupName ):
		"""
			\remarks	[abstract] set the group name for this layer instance
			\sa			layerName
			\param		layerName	<str>
			\return		<bool> success
		"""
		from blurdev import debug
		
		# when debugging, raise an error
		if ( debug.debugLevel() ):
			raise NotImplementedError
		
		return False
	
	def setHidden( self, state ):
		"""
			\remarks	set the hidden state for the objects on this layer
			\sa			hide, unhide, _nativeObjets, blur3d.api.Scene._hideNativeObjects
			\param		state	<bool>
			\return		<bool> success
		"""
		return self._scene._hideNativeObjects( self._nativeObjects(), state )
	
	def setSelected( self, state ):
		"""
			\remarks	sets the selected state of the objects on this layer
			\sa			deselect, setSelected, _nativeObjects, blur3d.api.Scene.setSelection
			\param		state	<bool>
			\return		<bool> success
		"""
		return self._scene._setNativeSelection( self._nativeObjects() )
	
	def unhide( self ):
		"""
			\remarks	unhides the objects on this layer
			\sa			hide, setHidden
			\return		<bool> success
		"""
		return self.setHidden(False)
	
	def unfreeze( self ):
		"""
			\remarks	unfreezes the objects on this layer
			\sa			freeze, setFrozen
			\return		<bool> success
		"""
		return self.setFrozen(False)


# register the symbol
from blur3d import api
api.registerSymbol( 'SceneObjectGroup', AbstractSceneObjectGroup, ifNotFound = True )