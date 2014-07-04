# ----------------------------------------------------------------------------
# error codes
# ----------------------------------------------------------------------------
IS_NO_SUCCESS                       = -1   # function call failed
IS_SUCCESS                          =  0   # function call succeeded
IS_INVALID_CAMERA_HANDLE            =  1   # camera handle is not valid or zero
IS_INVALID_HANDLE                   =  1   # a handle other than the camera handle is invalid

IS_IO_REQUEST_FAILED                =  2   # an io request to the driver failed
IS_CANT_OPEN_DEVICE                 =  3   # returned by is_InitCamera
IS_CANT_CLOSE_DEVICE                =  4
IS_CANT_SETUP_MEMORY                =  5
IS_NO_HWND_FOR_ERROR_REPORT         =  6
IS_ERROR_MESSAGE_NOT_CREATED        =  7
IS_ERROR_STRING_NOT_FOUND           =  8
IS_HOOK_NOT_CREATED                 =  9
IS_TIMER_NOT_CREATED                = 10
IS_CANT_OPEN_REGISTRY               = 11
IS_CANT_READ_REGISTRY               = 12
IS_CANT_VALIDATE_BOARD              = 13
IS_CANT_GIVE_BOARD_ACCESS           = 14
IS_NO_IMAGE_MEM_ALLOCATED           = 15
IS_CANT_CLEANUP_MEMORY              = 16
IS_CANT_COMMUNICATE_WITH_DRIVER     = 17
IS_FUNCTION_NOT_SUPPORTED_YET       = 18
IS_OPERATING_SYSTEM_NOT_SUPPORTED   = 19

IS_INVALID_VIDEO_IN                 = 20
IS_INVALID_IMG_SIZE                 = 21
IS_INVALID_ADDRESS                  = 22
IS_INVALID_VIDEO_MODE               = 23
IS_INVALID_AGC_MODE                 = 24
IS_INVALID_GAMMA_MODE               = 25
IS_INVALID_SYNC_LEVEL               = 26
IS_INVALID_CBARS_MODE               = 27
IS_INVALID_COLOR_MODE               = 28
IS_INVALID_SCALE_FACTOR             = 29
IS_INVALID_IMAGE_SIZE               = 30
IS_INVALID_IMAGE_POS                = 31
IS_INVALID_CAPTURE_MODE             = 32
IS_INVALID_RISC_PROGRAM             = 33
IS_INVALID_BRIGHTNESS               = 34
IS_INVALID_CONTRAST                 = 35
IS_INVALID_SATURATION_U             = 36
IS_INVALID_SATURATION_V             = 37
IS_INVALID_HUE                      = 38
IS_INVALID_HOR_FILTER_STEP          = 39
IS_INVALID_VERT_FILTER_STEP         = 40
IS_INVALID_EEPROM_READ_ADDRESS      = 41
IS_INVALID_EEPROM_WRITE_ADDRESS     = 42
IS_INVALID_EEPROM_READ_LENGTH       = 43
IS_INVALID_EEPROM_WRITE_LENGTH      = 44
IS_INVALID_BOARD_INFO_POINTER       = 45
IS_INVALID_DISPLAY_MODE             = 46
IS_INVALID_ERR_REP_MODE             = 47
IS_INVALID_BITS_PIXEL               = 48
IS_INVALID_MEMORY_POINTER           = 49

IS_FILE_WRITE_OPEN_ERROR            = 50
IS_FILE_READ_OPEN_ERROR             = 51
IS_FILE_READ_INVALID_BMP_ID         = 52
IS_FILE_READ_INVALID_BMP_SIZE       = 53
IS_FILE_READ_INVALID_BIT_COUNT      = 54
IS_WRONG_KERNEL_VERSION             = 55

IS_RISC_INVALID_XLENGTH             = 60
IS_RISC_INVALID_YLENGTH             = 61
IS_RISC_EXCEED_IMG_SIZE             = 62

# DirectDraw Mode errors
IS_DD_MAIN_FAILED                   = 70
IS_DD_PRIMSURFACE_FAILED            = 71
IS_DD_SCRN_SIZE_NOT_SUPPORTED       = 72
IS_DD_CLIPPER_FAILED                = 73
IS_DD_CLIPPER_HWND_FAILED           = 74
IS_DD_CLIPPER_CONNECT_FAILED        = 75
IS_DD_BACKSURFACE_FAILED            = 76
IS_DD_BACKSURFACE_IN_SYSMEM         = 77
IS_DD_MDL_MALLOC_ERR                = 78
IS_DD_MDL_SIZE_ERR                  = 79
IS_DD_CLIP_NO_CHANGE                = 80
IS_DD_PRIMMEM_NULL                  = 81
IS_DD_BACKMEM_NULL                  = 82
IS_DD_BACKOVLMEM_NULL               = 83
IS_DD_OVERLAYSURFACE_FAILED         = 84
IS_DD_OVERLAYSURFACE_IN_SYSMEM      = 85
IS_DD_OVERLAY_NOT_ALLOWED           = 86
IS_DD_OVERLAY_COLKEY_ERR            = 87
IS_DD_OVERLAY_NOT_ENABLED           = 88
IS_DD_GET_DC_ERROR                  = 89
IS_DD_DDRAW_DLL_NOT_LOADED          = 90
IS_DD_THREAD_NOT_CREATED            = 91
IS_DD_CANT_GET_CAPS                 = 92
IS_DD_NO_OVERLAYSURFACE             = 93
IS_DD_NO_OVERLAYSTRETCH             = 94
IS_DD_CANT_CREATE_OVERLAYSURFACE    = 95
IS_DD_CANT_UPDATE_OVERLAYSURFACE    = 96
IS_DD_INVALID_STRETCH               = 97

IS_EV_INVALID_EVENT_NUMBER          =100
IS_INVALID_MODE                     =101
IS_CANT_FIND_FALCHOOK               =102
IS_CANT_FIND_HOOK                   =102
IS_CANT_GET_HOOK_PROC_ADDR          =103
IS_CANT_CHAIN_HOOK_PROC             =104
IS_CANT_SETUP_WND_PROC              =105
IS_HWND_NULL                        =106
IS_INVALID_UPDATE_MODE              =107
IS_NO_ACTIVE_IMG_MEM                =108
IS_CANT_INIT_EVENT                  =109
IS_FUNC_NOT_AVAIL_IN_OS             =110
IS_CAMERA_NOT_CONNECTED             =111
IS_SEQUENCE_LIST_EMPTY              =112
IS_CANT_ADD_TO_SEQUENCE             =113
IS_LOW_OF_SEQUENCE_RISC_MEM         =114
IS_IMGMEM2FREE_USED_IN_SEQ          =115
IS_IMGMEM_NOT_IN_SEQUENCE_LIST      =116
IS_SEQUENCE_BUF_ALREADY_LOCKED      =117
IS_INVALID_DEVICE_ID                =118
IS_INVALID_BOARD_ID                 =119
IS_ALL_DEVICES_BUSY                 =120
IS_HOOK_BUSY                        =121
IS_TIMED_OUT                        =122
IS_NULL_POINTER                     =123
IS_WRONG_HOOK_VERSION               =124
IS_INVALID_PARAMETER                =125   # a parameter specified was invalid
IS_NOT_ALLOWED                      =126
IS_OUT_OF_MEMORY                    =127
IS_INVALID_WHILE_LIVE               =128
IS_ACCESS_VIOLATION                 =129   # an internal exception occurred
IS_UNKNOWN_ROP_EFFECT               =130
IS_INVALID_RENDER_MODE              =131
IS_INVALID_THREAD_CONTEXT           =132
IS_NO_HARDWARE_INSTALLED            =133
IS_INVALID_WATCHDOG_TIME            =134
IS_INVALID_WATCHDOG_MODE            =135
IS_INVALID_PASSTHROUGH_IN           =136
IS_ERROR_SETTING_PASSTHROUGH_IN     =137
IS_FAILURE_ON_SETTING_WATCHDOG      =138
IS_NO_USB20                         =139   # the usb port doesnt support usb 2.0
IS_CAPTURE_RUNNING                  =140   # there is already a capture running

IS_MEMORY_BOARD_ACTIVATED           =141   # operation could not execute while mboard is enabled
IS_MEMORY_BOARD_DEACTIVATED         =142   # operation could not execute while mboard is disabled
IS_NO_MEMORY_BOARD_CONNECTED        =143   # no memory board connected
IS_TOO_LESS_MEMORY                  =144   # image size is above memory capacity
IS_IMAGE_NOT_PRESENT                =145   # requested image is no longer present in the camera
IS_MEMORY_MODE_RUNNING              =146
IS_MEMORYBOARD_DISABLED             =147

IS_TRIGGER_ACTIVATED                =148   # operation could not execute while trigger is enabled
IS_WRONG_KEY                        =150
IS_CRC_ERROR                        =151
IS_NOT_YET_RELEASED                 =152   # this feature is not available yet
IS_NOT_CALIBRATED                   =153   # the camera is not calibrated
IS_WAITING_FOR_KERNEL               =154   # a request to the kernel exceeded
IS_NOT_SUPPORTED                    =155   # operation mode is not supported
IS_TRIGGER_NOT_ACTIVATED            =156   # operation could not execute while trigger is disabled
IS_OPERATION_ABORTED                =157
IS_BAD_STRUCTURE_SIZE               =158
IS_INVALID_BUFFER_SIZE              =159
IS_INVALID_PIXEL_CLOCK              =160
IS_INVALID_EXPOSURE_TIME            =161
IS_AUTO_EXPOSURE_RUNNING            =162
IS_CANNOT_CREATE_BB_SURF            =163   # error creating backbuffer surface
IS_CANNOT_CREATE_BB_MIX             =164   # backbuffer mixer surfaces can not be created
IS_BB_OVLMEM_NULL                   =165   # backbuffer overlay mem could not be locked
IS_CANNOT_CREATE_BB_OVL             =166   # backbuffer overlay mem could not be created
IS_NOT_SUPP_IN_OVL_SURF_MODE        =167   # function not supported in overlay surface mode
IS_INVALID_SURFACE                  =168   # surface invalid
IS_SURFACE_LOST                     =169   # surface has been lost
IS_RELEASE_BB_OVL_DC                =170   # error releasing backbuffer overlay DC
IS_BB_TIMER_NOT_CREATED             =171   # backbuffer timer could not be created
IS_BB_OVL_NOT_EN                    =172   # backbuffer overlay has not been enabled
IS_ONLY_IN_BB_MODE                  =173   # only possible in backbuffer mode
IS_INVALID_COLOR_FORMAT             =174   # invalid color format
IS_INVALID_WB_BINNING_MODE          =175   # invalid binning mode for AWB
IS_INVALID_I2C_DEVICE_ADDRESS       =176   # invalid I2C device address
IS_COULD_NOT_CONVERT                =177   # current image couldn't be converted
IS_TRANSFER_ERROR                   =178   # transfer failed
IS_PARAMETER_SET_NOT_PRESENT        =179   # the parameter set is not present
IS_INVALID_CAMERA_TYPE              =180   # the camera type in the ini file doesn't match
IS_INVALID_HOST_IP_HIBYTE           =181   # HIBYTE of host address is invalid
IS_CM_NOT_SUPP_IN_CURR_DISPLAYMODE  =182   # color mode is not supported in the current display mode
IS_NO_IR_FILTER                     =183
IS_STARTER_FW_UPLOAD_NEEDED         =184   # device starter firmware is not compatible    

IS_DR_LIBRARY_NOT_FOUND                 =185   # the DirectRender library could not be found
IS_DR_DEVICE_OUT_OF_MEMORY              =186   # insufficient graphics adapter video memory
IS_DR_CANNOT_CREATE_SURFACE             =187   # the image or overlay surface could not be created
IS_DR_CANNOT_CREATE_VERTEX_BUFFER       =188   # the vertex buffer could not be created
IS_DR_CANNOT_CREATE_TEXTURE             =189   # the texture could not be created
IS_DR_CANNOT_LOCK_OVERLAY_SURFACE       =190   # the overlay surface could not be locked
IS_DR_CANNOT_UNLOCK_OVERLAY_SURFACE     =191   # the overlay surface could not be unlocked
IS_DR_CANNOT_GET_OVERLAY_DC             =192   # cannot get the overlay surface DC
IS_DR_CANNOT_RELEASE_OVERLAY_DC         =193   # cannot release the overlay surface DC
IS_DR_DEVICE_CAPS_INSUFFICIENT          =194   # insufficient graphics adapter capabilities
IS_INCOMPATIBLE_SETTING                 =195   # Operation is not possible because of another incompatible setting
IS_DR_NOT_ALLOWED_WHILE_DC_IS_ACTIVE    =196   # user App still has DC handle.


# ----------------------------------------------------------------------------
# display mode selectors
# ----------------------------------------------------------------------------
IS_GET_DISPLAY_MODE               =  0x8000
IS_GET_DISPLAY_SIZE_X             =  0x8000
IS_GET_DISPLAY_SIZE_Y             =  0x8001
IS_GET_DISPLAY_POS_X              =  0x8000
IS_GET_DISPLAY_POS_Y              =  0x8001

IS_SET_DM_DIB                     =  1
IS_SET_DM_DIRECTDRAW              =  2
IS_SET_DM_DIRECT3D                =  4
IS_SET_DM_ALLOW_SYSMEM            =  0x40
IS_SET_DM_ALLOW_PRIMARY           =  0x80

# -- overlay display mode ---
IS_GET_DD_OVERLAY_SCALE           =  0x8000

IS_SET_DM_ALLOW_OVERLAY           =  0x100
IS_SET_DM_ALLOW_SCALING           =  0x200
IS_SET_DM_ALLOW_FIELDSKIP         =  0x400
IS_SET_DM_MONO                    =  0x800
IS_SET_DM_BAYER                   =  0x1000
IS_SET_DM_YCBCR                   =  0x4000

# -- backbuffer display mode ---
IS_SET_DM_BACKBUFFER              =  0x2000

# ----------------------------------------------------------------------------
# Image files types
# ----------------------------------------------------------------------------
IS_IMG_BMP                         = 0
IS_IMG_JPG                         = 1
IS_IMG_PNG                         = 2
IS_IMG_RAW                         = 4
IS_IMG_TIF                         = 8


# ----------------------------------------------------------------------------
# Auto Control Parameter
# ----------------------------------------------------------------------------
IS_SET_ENABLE_AUTO_GAIN             = 0x8800
IS_GET_ENABLE_AUTO_GAIN             = 0x8801
IS_SET_ENABLE_AUTO_SHUTTER          = 0x8802
IS_GET_ENABLE_AUTO_SHUTTER          = 0x8803
IS_SET_ENABLE_AUTO_WHITEBALANCE     = 0x8804
IS_GET_ENABLE_AUTO_WHITEBALANCE     = 0x8805
IS_SET_ENABLE_AUTO_FRAMERATE        = 0x8806
IS_GET_ENABLE_AUTO_FRAMERATE        = 0x8807
IS_SET_ENABLE_AUTO_SENSOR_GAIN      = 0x8808
IS_GET_ENABLE_AUTO_SENSOR_GAIN      = 0x8809
IS_SET_ENABLE_AUTO_SENSOR_SHUTTER   = 0x8810
IS_GET_ENABLE_AUTO_SENSOR_SHUTTER   = 0x8811
IS_SET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER  = 0x8812
IS_GET_ENABLE_AUTO_SENSOR_GAIN_SHUTTER  = 0x8813
IS_SET_ENABLE_AUTO_SENSOR_FRAMERATE     = 0x8814
IS_GET_ENABLE_AUTO_SENSOR_FRAMERATE     = 0x8815
IS_SET_ENABLE_AUTO_SENSOR_WHITEBALANCE  = 0x8816
IS_GET_ENABLE_AUTO_SENSOR_WHITEBALANCE  = 0x8817


IS_SET_AUTO_REFERENCE               = 0x8000
IS_GET_AUTO_REFERENCE               = 0x8001
IS_SET_AUTO_GAIN_MAX                = 0x8002
IS_GET_AUTO_GAIN_MAX                = 0x8003
IS_SET_AUTO_SHUTTER_MAX             = 0x8004
IS_GET_AUTO_SHUTTER_MAX             = 0x8005
IS_SET_AUTO_SPEED                   = 0x8006
IS_GET_AUTO_SPEED                   = 0x8007
IS_SET_AUTO_WB_OFFSET               = 0x8008
IS_GET_AUTO_WB_OFFSET               = 0x8009
IS_SET_AUTO_WB_GAIN_RANGE           = 0x800A
IS_GET_AUTO_WB_GAIN_RANGE           = 0x800B
IS_SET_AUTO_WB_SPEED                = 0x800C
IS_GET_AUTO_WB_SPEED                = 0x800D
IS_SET_AUTO_WB_ONCE                 = 0x800E
IS_GET_AUTO_WB_ONCE                 = 0x800F
IS_SET_AUTO_BRIGHTNESS_ONCE         = 0x8010
IS_GET_AUTO_BRIGHTNESS_ONCE         = 0x8011
IS_SET_AUTO_HYSTERESIS              = 0x8012
IS_GET_AUTO_HYSTERESIS              = 0x8013
IS_GET_AUTO_HYSTERESIS_RANGE        = 0x8014
IS_SET_AUTO_WB_HYSTERESIS           = 0x8015
IS_GET_AUTO_WB_HYSTERESIS           = 0x8016
IS_GET_AUTO_WB_HYSTERESIS_RANGE     = 0x8017
IS_SET_AUTO_SKIPFRAMES              = 0x8018
IS_GET_AUTO_SKIPFRAMES              = 0x8019
IS_GET_AUTO_SKIPFRAMES_RANGE        = 0x801A
IS_SET_AUTO_WB_SKIPFRAMES           = 0x801B
IS_GET_AUTO_WB_SKIPFRAMES           = 0x801C
IS_GET_AUTO_WB_SKIPFRAMES_RANGE     = 0x801D
IS_SET_SENS_AUTO_SHUTTER_PHOTOM             = 0x801E
IS_SET_SENS_AUTO_GAIN_PHOTOM                = 0x801F
IS_GET_SENS_AUTO_SHUTTER_PHOTOM             = 0x8020
IS_GET_SENS_AUTO_GAIN_PHOTOM                = 0x8021
IS_GET_SENS_AUTO_SHUTTER_PHOTOM_DEF         = 0x8022
IS_GET_SENS_AUTO_GAIN_PHOTOM_DEF            = 0x8023
IS_SET_SENS_AUTO_CONTRAST_CORRECTION        = 0x8024
IS_GET_SENS_AUTO_CONTRAST_CORRECTION        = 0x8025
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_RANGE  = 0x8026
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_INC    = 0x8027
IS_GET_SENS_AUTO_CONTRAST_CORRECTION_DEF    = 0x8028
IS_SET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE    = 0x8029
IS_GET_SENS_AUTO_CONTRAST_FDT_AOI_ENABLE    = 0x8030
IS_SET_SENS_AUTO_BACKLIGHT_COMP             = 0x8031
IS_GET_SENS_AUTO_BACKLIGHT_COMP             = 0x8032
IS_GET_SENS_AUTO_BACKLIGHT_COMP_RANGE       = 0x8033
IS_GET_SENS_AUTO_BACKLIGHT_COMP_INC         = 0x8034
IS_GET_SENS_AUTO_BACKLIGHT_COMP_DEF         = 0x8035
IS_SET_ANTI_FLICKER_MODE                    = 0x8036
IS_GET_ANTI_FLICKER_MODE                    = 0x8037
IS_GET_ANTI_FLICKER_MODE_DEF                = 0x8038

# ----------------------------------------------------------------------------
# Auto Control definitions
# ----------------------------------------------------------------------------
IS_MIN_AUTO_BRIGHT_REFERENCE        =   0
IS_MAX_AUTO_BRIGHT_REFERENCE        = 255
IS_DEFAULT_AUTO_BRIGHT_REFERENCE    = 128
IS_MIN_AUTO_SPEED                   =   0
IS_MAX_AUTO_SPEED                   = 100
IS_DEFAULT_AUTO_SPEED               =  50

IS_DEFAULT_AUTO_WB_OFFSET           =   0
IS_MIN_AUTO_WB_OFFSET               = -50
IS_MAX_AUTO_WB_OFFSET               =  50
IS_DEFAULT_AUTO_WB_SPEED            =  50
IS_MIN_AUTO_WB_SPEED                =   0
IS_MAX_AUTO_WB_SPEED                = 100
IS_MIN_AUTO_WB_REFERENCE            =   0
IS_MAX_AUTO_WB_REFERENCE            = 255

# ----------------------------------------------------------------------------
# color modes
# ----------------------------------------------------------------------------
IS_GET_COLOR_MODE                   = 0x8000

IS_SET_CM_RGB32                     = 0
IS_SET_CM_RGB24                     = 1
IS_SET_CM_RGB16                     = 2
IS_SET_CM_RGB15                     = 3
IS_SET_CM_Y8                        = 6
IS_SET_CM_RGB8                      = 7
IS_SET_CM_BAYER                     = 11
IS_SET_CM_UYVY                      = 12
IS_SET_CM_UYVY_MONO                 = 13
IS_SET_CM_UYVY_BAYER                = 14
IS_SET_CM_CBYCRY                    = 23

IS_SET_CM_RGBY                      = 24
IS_SET_CM_RGB30                     = 25
IS_SET_CM_Y12                       = 26
IS_SET_CM_BAYER12                   = 27
IS_SET_CM_Y16                       = 28
IS_SET_CM_BAYER16                   = 29

IS_CM_MODE_MASK                     = 0x007F

# planar vs packed format
IS_CM_FORMAT_PACKED                 = 0x0000
IS_CM_FORMAT_PLANAR                 = 0x2000
IS_CM_FORMAT_MASK                   = 0x2000

# BGR vs. RGB order
IS_CM_ORDER_BGR                     = 0x0000
IS_CM_ORDER_RGB                     = 0x0080
IS_CM_ORDER_MASK                    = 0x0080


# define compliant color format names
IS_CM_MONO8                 = IS_SET_CM_Y8                                              # occupies 8 Bit
IS_CM_MONO12                = IS_SET_CM_Y12                                             # occupies 16 Bit
IS_CM_MONO16                = IS_SET_CM_Y16                                             # occupies 16 Bit

IS_CM_BAYER_RG8             = IS_SET_CM_BAYER                                           # occupies 8 Bit
IS_CM_BAYER_RG12            = IS_SET_CM_BAYER12                                         # occupies 16 Bit
IS_CM_BAYER_RG16            = IS_SET_CM_BAYER16                                         # occupies 16 Bit

IS_CM_SENSOR_RAW8           = IS_SET_CM_BAYER                                           # occupies 8 Bit
IS_CM_SENSOR_RAW12          = IS_SET_CM_BAYER12                                         # occupies 16 Bit
IS_CM_SENSOR_RAW16          = IS_SET_CM_BAYER16                                         # occupies 16 Bit

IS_CM_BGR555_PACKED         = (IS_SET_CM_RGB15 | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 16 Bit
IS_CM_BGR565_PACKED         = (IS_SET_CM_RGB16 | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 16 Bit

IS_CM_RGB8_PACKED           = (IS_SET_CM_RGB24 | IS_CM_ORDER_RGB | IS_CM_FORMAT_PACKED) # occupies 24 Bit
IS_CM_BGR8_PACKED           = (IS_SET_CM_RGB24 | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 24 Bit
IS_CM_RGBA8_PACKED          = (IS_SET_CM_RGB32 | IS_CM_ORDER_RGB | IS_CM_FORMAT_PACKED) # occupies 32 Bit
IS_CM_BGRA8_PACKED          = (IS_SET_CM_RGB32 | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 32 Bit
IS_CM_RGBY8_PACKED          = (IS_SET_CM_RGBY  | IS_CM_ORDER_RGB | IS_CM_FORMAT_PACKED) # occupies 32 Bit
IS_CM_BGRY8_PACKED          = (IS_SET_CM_RGBY  | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 32 Bit
IS_CM_RGB10V2_PACKED        = (IS_SET_CM_RGB30 | IS_CM_ORDER_RGB | IS_CM_FORMAT_PACKED) # occupies 32 Bit
IS_CM_BGR10V2_PACKED        = (IS_SET_CM_RGB30 | IS_CM_ORDER_BGR | IS_CM_FORMAT_PACKED) # occupies 32 Bit

IS_CM_YUV422_PACKED         = 0 # no compliant version
IS_CM_UYVY_PACKED           = (IS_SET_CM_UYVY | IS_CM_FORMAT_PACKED)                    # occupies 16 Bit
IS_CM_UYVY_MONO_PACKED      = (IS_SET_CM_UYVY_MONO | IS_CM_FORMAT_PACKED)
IS_CM_UYVY_BAYER_PACKED     = (IS_SET_CM_UYVY_BAYER | IS_CM_FORMAT_PACKED)
IS_CM_CBYCRY_PACKED         = (IS_SET_CM_CBYCRY | IS_CM_FORMAT_PACKED)                  # occupies 16 Bit

IS_CM_RGB8_PLANAR           = 0 # no compliant version
IS_CM_RGB12_PLANAR          = 0 # no compliant version
IS_CM_RGB16_PLANAR          = 0 # no compliant version


IS_CM_ALL_POSSIBLE                  = 0xFFFF

# ----------------------------------------------------------------------------
# event constants
# ----------------------------------------------------------------------------
IS_SET_EVENT_ODD                    = 0
IS_SET_EVENT_EVEN                   = 1
IS_SET_EVENT_FRAME                  = 2
IS_SET_EVENT_EXTTRIG                = 3
IS_SET_EVENT_VSYNC                  = 4
IS_SET_EVENT_SEQ                    = 5
IS_SET_EVENT_STEAL                  = 6
IS_SET_EVENT_VPRES                  = 7
IS_SET_EVENT_TRANSFER_FAILED        = 8
IS_SET_EVENT_DEVICE_RECONNECTED     = 9
IS_SET_EVENT_MEMORY_MODE_FINISH     = 10
IS_SET_EVENT_FRAME_RECEIVED         = 11
IS_SET_EVENT_WB_FINISHED            = 12
IS_SET_EVENT_AUTOBRIGHTNESS_FINISHED = 13

IS_SET_EVENT_REMOVE                 = 128
IS_SET_EVENT_REMOVAL                = 129
IS_SET_EVENT_NEW_DEVICE             = 130
IS_SET_EVENT_STATUS_CHANGED         = 131


# ----------------------------------------------------------------------------
# live/freeze parameters
# ----------------------------------------------------------------------------
IS_GET_LIVE                         = 0x8000

IS_WAIT                             = 0x0001
IS_DONT_WAIT                        = 0x0000
IS_FORCE_VIDEO_STOP                 = 0x4000
IS_FORCE_VIDEO_START                = 0x4000
IS_USE_NEXT_MEM                     = 0x8000

# ----------------------------------------------------------------------------
# Timing
# ----------------------------------------------------------------------------

# pixelclock
IS_GET_PIXEL_CLOCK                  = 0x8000
IS_GET_DEFAULT_PIXEL_CLK            = 0x8001
IS_GET_PIXEL_CLOCK_INC              = 0x8005

# frame rate
IS_GET_FRAMERATE                    = 0x8000
IS_GET_DEFAULT_FRAMERATE            = 0x8001

# exposure
IS_GET_EXPOSURE_TIME                = 0x8000
IS_GET_DEFAULT_EXPOSURE             = 0x8001
IS_GET_EXPOSURE_MIN_VALUE           = 0x8002
IS_GET_EXPOSURE_MAX_VALUE           = 0x8003
IS_GET_EXPOSURE_INCREMENT           = 0x8004
IS_GET_EXPOSURE_FINE_INCREMENT      = 0x8005