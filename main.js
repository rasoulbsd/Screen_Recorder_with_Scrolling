const electron = require ('electron')  // imports electron
const path = require ('path') // imports path module
const {app, Menu, Tray} = electron // imports menu and tray modules
const regedit = require('regedit')
const cmd=require('node-cmd');
const { isBoolean } = require('util');


const path2 = 'C:\\Users\\Public\\Documents\\Privacy_Manager\\Status.txt';

var mic_status = 0, camera_status = 0, loc_status = 0, bluetooth_status = 0, all_status = 0;

var tray
app.on('ready', _ => {
    tray = new Tray (path.join ('.', '/docs/logo/logo.ico' ) ) // sets tray icon image
    const contextMenu = Menu.buildFromTemplate([   // define menu items
      {
          label: 'Mute:',
          type : "normal",
      },
      {
          type : "separator",
      },
        {
            label: 'All',
            type : "checkbox",
            click:  ()  => {
                if(all_status == 1){
                  cmd.run('cscript.exe //NoLogo ./vbs/microphone/mic_off.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/webcam/camera_off.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/bluetooth/bluetooth_off.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/location/loc_off.vbs');

                  mic_status = 0, camera_status = 0, bluetooth_status = 0, loc_status = 0, all_status = 0;
                }
                else if(all_status == 0){
                  cmd.run('cscript.exe //NoLogo ./vbs/microphone/mic_on.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/webcam/camera_on.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/bluetooth/bluetooth_on.vbs');
                  cmd.run('cscript.exe //NoLogo ./vbs/location/loc_on.vbs');

                  mic_status = 1, camera_status = 1, bluetooth_status = 1, loc_status = 1, all_status = 1;
                }
                else{
                    console.log("There was an Error");
                    app.quit();
                }
                console.log("All Status: " + all_status);
            },
        },
        {
            label: 'Mic',
            type : "checkbox",
            click:  ()  => {
                if(mic_status == 1){
                    cmd.run('cscript.exe //NoLogo ./vbs/microphone/mic_off.vbs');
                    mic_status = 0;}
                else if(mic_status == 0){
                    cmd.run('cscript.exe //NoLogo ./vbs/microphone/mic_on.vbs');
                    mic_status = 1;}
                else{
                    console.log("There was an Error");
                    app.quit();
                }
                console.log("Mic Status: " + mic_status);
            },
        },
        {
            label: 'Webcam',
            type : "checkbox",
            click:  ()  => {
                if(camera_status == 1){
                    cmd.run('cscript.exe //NoLogo ./vbs/webcam/camera_off.vbs');
                    camera_status = 0;}
                else if(camera_status == 0){
                    cmd.run('cscript.exe //NoLogo ./vbs/webcam/camera_on.vbs');
                    camera_status = 1;}
                else{
                    console.log("There was an Error");
                    app.quit();
                }
                console.log("Camera Status: " + camera_status);
            },
        },
        {
            label: 'Location',
            type : "checkbox",
            click:  ()  => {
                if(loc_status == 1){
                    cmd.run('cscript.exe //NoLogo ./vbs/location/loc_off.vbs');
                    loc_status = 0;}
                else if(loc_status == 0){
                    cmd.run('cscript.exe //NoLogo ./vbs/location/loc_on.vbs');
                    loc_status = 1;}
                else{
                    console.log("There was an Error");
                    app.quit();
                }
                console.log("Location Status: " + loc_status);
            },
        },
        {
            label: 'Bluetooth',
            type : "checkbox",
            click:  ()  => {
                if(bluetooth_status == 1){
                    cmd.run('cscript.exe //NoLogo ./vbs/bluetooth/bluetooth_off.vbs');
                    bluetooth_status = 0;}
                else if(bluetooth_status == 0){
                    cmd.run('cscript.exe //NoLogo ./vbs/bluetooth/bluetooth_on.vbs');
                    bluetooth_status = 1;}
                else{
                    console.log("There was an Error");
                    app.quit();
                }
                console.log("Bluetooth Status: " + bluetooth_status);
            },
        },
        {
            type : "separator",
        },
        {
        label: 'Exit',
        type : "normal",
        click: () => app.quit(),
        },
    ])
    tray.setContextMenu(contextMenu)
})
