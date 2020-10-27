const {
    app,
    BrowserWindow,
    screen
} = require('electron')

let mainWin

function createWindow(screenWidth, screenHeight) {
    // console.log(screenWidth, screenHeight)
    const splashScreen = new BrowserWindow({
        width: Math.round(screenWidth*0.4),
        height: Math.round(screenHeight*0.4),
        frame: false,
        show: false,
        alwaysOnTop: true
    })

    // splashScreen.webContents.openDevTools()

    splashScreen.loadFile('./contents/splash.html')
    splashScreen.on('ready-to-show', (timeSplashShow) => {
        splashScreen.show()
    })

    const mainWin = new BrowserWindow({
        width: 1280,
        height: 720,
        show: false,
        frame: false,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // mainWin.loadFile('./contents/index.html')
    // mainWin.loadURL('https://www.runoob.com')
    // mainWin.loadURL('https://www.youtube.com')
    // mainWin.loadURL('https://www.bilibili.com')
    mainWin.loadURL('http://localhost:8080')
    // win.webContents.openDevTools()

    mainWin.on('ready-to-show', () => {
        setTimeout(() => {
            splashScreen.destroy()
            mainWin.show()
        }, 2000)
    })
}

app.on('ready', () => {
    const {width: screenWidth, height: screenHeight} = screen.getPrimaryDisplay().workArea
    createWindow(screenWidth, screenHeight)
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        const {width: screenWidth, height: screenHeight} = screen.getPrimaryDisplay().workArea
        createWindow(screenWidth, screenHeight)
    }
})