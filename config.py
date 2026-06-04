# config.py
import torch

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model
SEQ_LEN = 64
D_MODEL = 128
NHEAD = 4
NUM_LAYERS = 4
DIM_FEEDFORWARD = 512
DROPOUT = 0.1
PATCH_SIZE = 16
IMAGE_SIZE = 224
NUM_CLASSES = 3

# Training
BATCH_SIZE = 32
LR = 1e-4
EPOCHS = 20
MC_DROPOUT_SAMPLES = 30

# SMC
SWING_STRENGTH = 5
ORDER_BLOCK_LOOKBACK = 3
LIQUIDITY_SWEEP_THRESH = 0.005

# Trading / Backtest
INITIAL_CAPITAL = 1000.0      # ← spot starting balance
RISK_PER_TRADE = 0.02
MAX_DRAWDOWN = 0.25
SL_ATR_MULT = 1.5
TP_ATR_MULT = 2.0

# Multi-timeframe
TIMEFRAMES = ["1m", "5m", "15m", "1h", "4h", "1d"]