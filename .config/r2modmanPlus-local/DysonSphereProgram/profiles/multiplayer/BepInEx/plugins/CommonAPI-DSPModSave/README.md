# DSP Mod Save

This library allows to store mod save data separately from vanilla saves. It works by storing a separate file along each save file. In that file data of all mods is stored.

## Installation
### With Mod Manager

Simply open the mod manager (if you don't have it install it [here](https://dsp.thunderstore.io/package/ebkr/r2modman/)), select **DSP Mod Save by CommonAPI**, then **Download**.

If prompted to download with dependencies, select `Yes`.

Then just click **Start modded**, and the game will run with the mod installed.

### Manually
Install BepInEx from [here](https://dsp.thunderstore.io/package/xiaoye97/BepInEx/)<br/>

Unzip all files into `Dyson Sphere Program/BepInEx/plugins/DSPModSave/`. (Create folder named `DSPModSave`)<br/>

## Developing using DSP Mod Save
If you are a mod developer and want to use this library:
- Add DSPModSave to your references. You can use [this nuget](https://www.nuget.org/packages/DysonSphereProgram.Modding.DSPModSave/) to do so.
- Implement `IModCanSave` interface in your plugin class:
```cs
[BepInPlugin(GUID, NAME, VERSION)]

[BepInDependency(DSPModSavePlugin.MODGUID)]
public class MyPlugin : BaseUnityPlugin
{
    public const string MODID = "myplugin";
    public const string GUID = "org.myname.plugin." + MODID;
    public const string NAME = "My Plugin";
    
    public void Import(BinaryReader r)
    {
        // Load your saved data here
    }

    public void Export(BinaryWriter w)
    {
        // Save your data here
    }

    public void IntoOtherSave()
    {
        // Initialize here. This method will only be called if there is no saved data.
    }
}
```
- Don't forget to include `CommonAPI-DSPModSave-1.1.0` to your mod manifest file.

Originally released by crecheng [here](https://dsp.thunderstore.io/package/crecheng/DSPModSave/). Reuploading since crecheng no longer maintains the mod.

## Feedback and Bug Report
Feel free to contact me via Discord (Kremnev8#3756) for any feedback, bug-reports or suggestions.

## Changelog
### v1.1.4
- Now whenever a mod has errors saving/loading save data, a popup notifying the user will appear.
### v1.1.3
- Added plugin catergories on Thunderstore page.
### v1.1.1-2
- Added ability to manually request to be added to mod save list. Useful for testing with ScriptEngine.
### v1.1.0
- Reuploaded under CommonAPI name
- Fixed that `IntoOtherSave` was called too early
- Fixed that `IntoOtherSave` was not called if mod had no saved data in savefile
### v1.0.0-1.0.2
- Initial Release