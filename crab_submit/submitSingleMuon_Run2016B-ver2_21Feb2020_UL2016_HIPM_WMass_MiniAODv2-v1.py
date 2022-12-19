from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'SingleMuon_Run2016B-ver2_21Feb2020_UL2016_HIPM_WMass_MiniAODv2-v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.numCores = 1
config.JobType.maxMemoryMB = 2000
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../configs/NanoV9DataPreVFP_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/SingleMuon/Run2016B-ver2_21Feb2020_UL2016_HIPM_WMass_MiniAODv2-v1/MINIAOD'

config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 14
config.Data.outLFNDirBase = '/store/group/cmst3/group/wmass/w-mass-13TeV/NanoAOD' 
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoV9DataPreVFP_TrackFitV709_NanoProdv2'
config.Data.inputDBS = 'global'
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'
