# -*- coding: cp936 -*-
import os,sys


table1 = [
0x14,  0x52,  0x24,  0x8D,  0x6A,  0x58,  0x68,  0x86,
0x3D,  0xB0,  0x0C,  0xA0,  0xA9,  0xD7,  0xFA,  0xF6,
0x8E,  0x01,  0xC9,  0x4C,  0x79,  0x4A,  0x3B,  0xCA,
0x74,  0x84,  0xED,  0x2D,  0x45,  0xC8,  0xCC,  0x28,
0x30,  0xD3,  0xAC,  0xC5,  0xB6,  0x9B,  0xB1,  0xCF,
0xB2,  0x7D,  0x85,  0xFE,  0x72,  0xE1,  0xF3,  0x6F,
0xA6,  0xFF,  0x8F,  0x77,  0x59,  0xDC,  0x9F,  0x0D,
0xF4,  0x47,  0xF2,  0xAF,  0xC2,  0x40,  0xDE,  0xAB,
0xA2,  0x7E,  0x48,  0xFC,  0x00,  0x6B,  0xF8,  0x6E,
0x3C,  0x54,  0x43,  0x96,  0x44,  0x83,  0xCB,  0x1D,
0xD0,  0x23,  0x42,  0x1C,  0x60,  0xC6,  0x6C,  0xB4,
0xBC,  0x81,  0xD8,  0x87,  0x99,  0x03,  0x91,  0xF0,
0x90,  0x76,  0x4E,  0x62,  0x18,  0x5D,  0xCD,  0x89,
0x5F,  0x39,  0x3E,  0x9D,  0xBB,  0x2E,  0x6D,  0x2A,
0xC0,  0x4D,  0x22,  0x56,  0x10,  0x71,  0x5A,  0x4B,
0x50,  0xA4,  0xD9,  0x25,  0xA1,  0x69,  0x8C,  0x38,
0xC1,  0xEB,  0xEE,  0x55,  0xA7,  0xF5,  0x34,  0xE7,
0x49,  0x27,  0xE5,  0x1A,  0xD4,  0x97,  0x8A,  0x16,
0x65,  0x06,  0x17,  0xC3,  0x7A,  0xD5,  0xDA,  0xEF,
0x36,  0x1F,  0x94,  0x07,  0xCE,  0x5B,  0x7F,  0x2B,
0x80,  0x2C,  0xBF,  0xC7,  0xEC,  0x9A,  0xF7,  0xF1,
0x53,  0x64,  0xB9,  0x9E,  0x95,  0x57,  0x0F,  0x15,
0xD1,  0x2F,  0xDF,  0x7C,  0x32,  0x11,  0x63,  0x51,
0xFB,  0x82,  0x31,  0x33,  0xE8,  0xE4,  0x9C,  0x0E,
0x29,  0x21,  0xA5,  0x0B,  0x7B,  0x73,  0x78,  0x02,
0x0A,  0xB3,  0x98,  0xE6,  0x37,  0x75,  0x20,  0x66,
0xE0,  0xE9,  0xBD,  0x19,  0xA8,  0xE3,  0x88,  0xDB,
0x1B,  0xAE,  0xE2,  0x26,  0x3F,  0xB8,  0x12,  0xAA,
0xAD,  0x1E,  0xD2,  0x67,  0x5C,  0xC4,  0xF9,  0x8B,
0xBA,  0x4F,  0x70,  0xA3,  0x61,  0x3A,  0xBE,  0x05,
0x09,  0x92,  0x41,  0xD6,  0xFD,  0x46,  0xDD,  0xB7,
0xEA,  0x13,  0xB5,  0x35,  0x08,  0x04,  0x93,  0x5E,
]

detable1 = [
0x44,  0x11,  0xC7,  0x5D,  0xFD,  0xEF,  0x91,  0x9B,
0xFC,  0xF0,  0xC8,  0xC3,  0x0A,  0x37,  0xBF,  0xAE,
0x74,  0xB5,  0xDE,  0xF9,  0x00,  0xAF,  0x8F,  0x92,
0x64,  0xD3,  0x8B,  0xD8,  0x53,  0x4F,  0xE1,  0x99,
0xCE,  0xC1,  0x72,  0x51,  0x02,  0x7B,  0xDB,  0x89,
0x1F,  0xC0,  0x6F,  0x9F,  0xA1,  0x1B,  0x6D,  0xB1,
0x20,  0xBA,  0xB4,  0xBB,  0x86,  0xFB,  0x98,  0xCC,
0x7F,  0x69,  0xED,  0x16,  0x48,  0x08,  0x6A,  0xDC,
0x3D,  0xF2,  0x52,  0x4A,  0x4C,  0x1C,  0xF5,  0x39,
0x42,  0x88,  0x15,  0x77,  0x13,  0x71,  0x62,  0xE9,
0x78,  0xB7,  0x01,  0xA8,  0x49,  0x83,  0x73,  0xAD,
0x05,  0x34,  0x76,  0x9D,  0xE4,  0x65,  0xFF,  0x68,
0x54,  0xEC,  0x63,  0xB6,  0xA9,  0x90,  0xCF,  0xE3,
0x06,  0x7D,  0x04,  0x45,  0x56,  0x6E,  0x47,  0x2F,
0xEA,  0x75,  0x2C,  0xC5,  0x18,  0xCD,  0x61,  0x33,
0xC6,  0x14,  0x94,  0xC4,  0xB3,  0x29,  0x41,  0x9E,
0xA0,  0x59,  0xB9,  0x4D,  0x19,  0x2A,  0x07,  0x5B,
0xD6,  0x67,  0x8E,  0xE7,  0x7E,  0x03,  0x10,  0x32,
0x60,  0x5E,  0xF1,  0xFE,  0x9A,  0xAC,  0x4B,  0x8D,
0xCA,  0x5C,  0xA5,  0x25,  0xBE,  0x6B,  0xAB,  0x36,
0x0B,  0x7C,  0x40,  0xEB,  0x79,  0xC2,  0x30,  0x84,
0xD4,  0x0C,  0xDF,  0x3F,  0x22,  0xE0,  0xD9,  0x3B,
0x09,  0x26,  0x28,  0xC9,  0x57,  0xFA,  0x24,  0xF7,
0xDD,  0xAA,  0xE8,  0x6C,  0x58,  0xD2,  0xEE,  0xA2,
0x70,  0x80,  0x3C,  0x93,  0xE5,  0x23,  0x55,  0xA3,
0x1D,  0x12,  0x17,  0x4E,  0x1E,  0x66,  0x9C,  0x27,
0x50,  0xB0,  0xE2,  0x21,  0x8C,  0x95,  0xF3,  0x0D,
0x5A,  0x7A,  0x96,  0xD7,  0x35,  0xF6,  0x3E,  0xB2,
0xD0,  0x2D,  0xDA,  0xD5,  0xBD,  0x8A,  0xCB,  0x87,
0xBC,  0xD1,  0xF8,  0x81,  0xA4,  0x1A,  0x82,  0x97,
0x5F,  0xA7,  0x3A,  0x2E,  0x38,  0x85,  0x0F,  0xA6,
0x46,  0xE6,  0x0E,  0xB8,  0x43,  0xF4,  0x2B,  0x31,
]

table2 = [
0x28,  0xC9,  0xBB,  0x27,  0x71,  0x2A,  0xEF,  0x57,
0xB4,  0x77,  0x9D,  0x62,  0x2E,  0x4C,  0x8D,  0xA8,
0x0D,  0xD0,  0xD1,  0xF4,  0xEE,  0x41,  0xE1,  0xA6,
0xD2,  0x86,  0x0F,  0xDB,  0xC1,  0xD7,  0x5F,  0xCC,
0x11,  0xB6,  0x30,  0x3C,  0x1C,  0x08,  0x8F,  0x51,
0x9C,  0x9A,  0x4E,  0x76,  0x73,  0x07,  0x09,  0xBF,
0x01,  0x44,  0xF2,  0xD4,  0x4D,  0x18,  0x6A,  0x48,
0xF6,  0x8C,  0x70,  0xE9,  0x97,  0x22,  0xF5,  0x37,
0xB2,  0x99,  0xF9,  0x4F,  0xF0,  0xAB,  0x52,  0xB8,
0xAC,  0xFB,  0x0E,  0xFF,  0x98,  0xF7,  0xBD,  0xA7,
0x4A,  0x32,  0x67,  0x24,  0x8A,  0x94,  0xDF,  0xAF,
0x31,  0x23,  0x47,  0xC0,  0x29,  0xAD,  0xEB,  0xC3,
0x2C,  0x65,  0x1A,  0xE6,  0x05,  0x53,  0x5D,  0x1D,
0x4B,  0x1E,  0xBE,  0xA9,  0x9E,  0x12,  0x96,  0xF3,
0x0B,  0x78,  0x6D,  0xBA,  0x7D,  0x5C,  0xE0,  0xFD,
0xF1,  0xC5,  0xE8,  0xBC,  0xA4,  0xEC,  0x7B,  0x55,
0x8B,  0x50,  0x3E,  0xFE,  0x9F,  0xB3,  0xC6,  0x2F,
0x81,  0x39,  0xF8,  0x6F,  0x46,  0x95,  0x64,  0xC8,
0x35,  0x40,  0x5A,  0x6B,  0x66,  0xDA,  0x20,  0xE4,
0xFC,  0xB7,  0x2D,  0xCD,  0xA2,  0x90,  0x83,  0xB0,
0x79,  0x02,  0xA1,  0x56,  0x19,  0xCE,  0x38,  0x25,
0x75,  0xDD,  0x7F,  0x6E,  0x88,  0xCF,  0xD9,  0x60,
0xCA,  0x0A,  0xB5,  0x45,  0x00,  0x85,  0xE2,  0x87,
0x5B,  0x42,  0x14,  0x82,  0xD6,  0xEA,  0x43,  0x59,
0xB1,  0xED,  0x58,  0xB9,  0xC2,  0x13,  0x72,  0x3A,
0x1F,  0x15,  0x80,  0x2B,  0xA0,  0xC4,  0x54,  0x6C,
0x74,  0x33,  0x5E,  0x26,  0x1B,  0x61,  0xFA,  0x92,
0xCB,  0x0C,  0x7A,  0xE3,  0xE5,  0x8E,  0x63,  0x68,
0x03,  0x69,  0x91,  0xE7,  0x7C,  0xA5,  0x84,  0x10,
0xDE,  0x17,  0xAE,  0xD3,  0x9B,  0x7E,  0xAA,  0x06,
0x04,  0x3D,  0xDC,  0x16,  0x36,  0x89,  0x3B,  0xD8,
0xC7,  0xA3,  0x34,  0x49,  0xD5,  0x3F,  0x21,  0x93,
]

detable2 = [
0xB4,  0x30,  0xA1,  0xE0,  0xF0,  0x64,  0xEF,  0x2D,
0x25,  0x2E,  0xB1,  0x70,  0xD9,  0x10,  0x4A,  0x1A,
0xE7,  0x20,  0x6D,  0xC5,  0xBA,  0xC9,  0xF3,  0xE9,
0x35,  0xA4,  0x62,  0xD4,  0x24,  0x67,  0x69,  0xC8,
0x96,  0xFE,  0x3D,  0x59,  0x53,  0xA7,  0xD3,  0x03,
0x00,  0x5C,  0x05,  0xCB,  0x60,  0x9A,  0x0C,  0x87,
0x22,  0x58,  0x51,  0xD1,  0xFA,  0x90,  0xF4,  0x3F,
0xA6,  0x89,  0xC7,  0xF6,  0x23,  0xF1,  0x82,  0xFD,
0x91,  0x15,  0xB9,  0xBE,  0x31,  0xB3,  0x8C,  0x5A,
0x37,  0xFB,  0x50,  0x68,  0x0D,  0x34,  0x2A,  0x43,
0x81,  0x27,  0x46,  0x65,  0xCE,  0x7F,  0xA3,  0x07,
0xC2,  0xBF,  0x92,  0xB8,  0x75,  0x66,  0xD2,  0x1E,
0xAF,  0xD5,  0x0B,  0xDE,  0x8E,  0x61,  0x94,  0x52,
0xDF,  0xE1,  0x36,  0x93,  0xCF,  0x72,  0xAB,  0x8B,
0x3A,  0x04,  0xC6,  0x2C,  0xD0,  0xA8,  0x2B,  0x09,
0x71,  0xA0,  0xDA,  0x7E,  0xE4,  0x74,  0xED,  0xAA,
0xCA,  0x88,  0xBB,  0x9E,  0xE6,  0xB5,  0x19,  0xB7,
0xAC,  0xF5,  0x54,  0x80,  0x39,  0x0E,  0xDD,  0x26,
0x9D,  0xE2,  0xD7,  0xFF,  0x55,  0x8D,  0x6E,  0x3C,
0x4C,  0x41,  0x29,  0xEC,  0x28,  0x0A,  0x6C,  0x84,
0xCC,  0xA2,  0x9C,  0xF9,  0x7C,  0xE5,  0x17,  0x4F,
0x0F,  0x6B,  0xEE,  0x45,  0x48,  0x5D,  0xEA,  0x57,
0x9F,  0xC0,  0x40,  0x85,  0x08,  0xB2,  0x21,  0x99,
0x47,  0xC3,  0x73,  0x02,  0x7B,  0x4E,  0x6A,  0x2F,
0x5B,  0x1C,  0xC4,  0x5F,  0xCD,  0x79,  0x86,  0xF8,
0x8F,  0x01,  0xB0,  0xD8,  0x1F,  0x9B,  0xA5,  0xAD,
0x11,  0x12,  0x18,  0xEB,  0x33,  0xFC,  0xBC,  0x1D,
0xF7,  0xAE,  0x95,  0x1B,  0xF2,  0xA9,  0xE8,  0x56,
0x76,  0x16,  0xB6,  0xDB,  0x97,  0xDC,  0x63,  0xE3,
0x7A,  0x3B,  0xBD,  0x5E,  0x7D,  0xC1,  0x14,  0x06,
0x44,  0x78,  0x32,  0x6F,  0x13,  0x3E,  0x38,  0x4D,
0x8A,  0x42,  0xD6,  0x49,  0x98,  0x77,  0x83,  0x4B,
]

table3 = [
0x40,  0x50,  0x78,  0x7A,  0x29,  0x88,  0xF7,  0x06,
0x21,  0x09,  0xF3,  0x5C,  0x95,  0xAE,  0x66,  0x12,
0x8F,  0x85,  0xC8,  0x5A,  0xBF,  0x33,  0x3D,  0x86,
0x90,  0x8C,  0xED,  0xD5,  0x8B,  0xA4,  0xC5,  0xC7,
0xEA,  0xF6,  0x79,  0x1E,  0x3C,  0xBA,  0x97,  0x4E,
0x38,  0x60,  0x08,  0xDD,  0xFA,  0xB3,  0xDE,  0x77,
0x81,  0x41,  0x19,  0xF4,  0x52,  0x6B,  0xFF,  0xD8,
0x2A,  0xC2,  0xBC,  0xB9,  0xE7,  0x91,  0xE9,  0x54,
0x82,  0xAD,  0x7E,  0x11,  0x35,  0x93,  0xB0,  0xA1,
0x18,  0xC4,  0x53,  0x0A,  0x74,  0x2F,  0xE2,  0x17,
0x98,  0x0C,  0x70,  0x92,  0x47,  0x64,  0x16,  0xFE,
0x75,  0x83,  0x37,  0x8D,  0x07,  0x72,  0x25,  0x04,
0xB7,  0xC9,  0xCE,  0x0E,  0x9E,  0xEB,  0xCF,  0xB1,
0xDB,  0x71,  0x56,  0xAF,  0x39,  0xF0,  0xBB,  0xBD,
0x46,  0x32,  0xE6,  0x9F,  0x4F,  0x1B,  0x4D,  0x68,
0xF2,  0x4B,  0x2E,  0xCB,  0x20,  0xD2,  0x0B,  0xA5,
0xEE,  0xE1,  0xA9,  0x2B,  0x84,  0x14,  0x67,  0x63,
0x6F,  0x3E,  0x7F,  0xFD,  0xB6,  0xFC,  0x55,  0x7C,
0x5F,  0xF8,  0x4C,  0x65,  0x2C,  0x30,  0xEF,  0x48,
0xD7,  0x0D,  0x0F,  0x1A,  0x5E,  0xC0,  0x3A,  0x57,
0x6A,  0x31,  0x00,  0xF1,  0x59,  0x10,  0xB8,  0x9A,
0x43,  0x73,  0xA3,  0x6E,  0x26,  0x1D,  0x13,  0x15,
0x89,  0x5D,  0xDA,  0x61,  0xD1,  0x6C,  0xD3,  0xE0,
0xD9,  0x1F,  0xD4,  0x49,  0xEC,  0xE3,  0xD0,  0x34,
0x36,  0xC6,  0x24,  0xE4,  0xF5,  0xAA,  0x9B,  0xB2,
0x4A,  0xDF,  0xAC,  0x96,  0xDC,  0xE8,  0xA0,  0xF9,
0xC1,  0x9C,  0xCA,  0x9D,  0x27,  0xC3,  0xBE,  0x87,
0x28,  0xCC,  0x99,  0xE5,  0x45,  0x58,  0x94,  0x23,
0x22,  0xFB,  0x02,  0x01,  0x03,  0x8A,  0x7B,  0xB5,
0x1C,  0xA7,  0x44,  0xCD,  0xA2,  0x51,  0x8E,  0x3F,
0x42,  0xD6,  0x69,  0xAB,  0x62,  0x3B,  0x7D,  0xA6,
0x05,  0x2D,  0xA8,  0x80,  0x6D,  0xB4,  0x76,  0x5B,
]

detable3 = [
0xA2,  0xE3,  0xE2,  0xE4,  0x5F,  0xF8,  0x07,  0x5C,
0x2A,  0x09,  0x4B,  0x7E,  0x51,  0x99,  0x63,  0x9A,
0xA5,  0x43,  0x0F,  0xAE,  0x85,  0xAF,  0x56,  0x4F,
0x48,  0x32,  0x9B,  0x75,  0xE8,  0xAD,  0x23,  0xB9,
0x7C,  0x08,  0xE0,  0xDF,  0xC2,  0x5E,  0xAC,  0xD4,
0xD8,  0x04,  0x38,  0x83,  0x94,  0xF9,  0x7A,  0x4D,
0x95,  0xA1,  0x71,  0x15,  0xBF,  0x44,  0xC0,  0x5A,
0x28,  0x6C,  0x9E,  0xF5,  0x24,  0x16,  0x89,  0xEF,
0x00,  0x31,  0xF0,  0xA8,  0xEA,  0xDC,  0x70,  0x54,
0x97,  0xBB,  0xC8,  0x79,  0x92,  0x76,  0x27,  0x74,
0x01,  0xED,  0x34,  0x4A,  0x3F,  0x8E,  0x6A,  0x9F,
0xDD,  0xA4,  0x13,  0xFF,  0x0B,  0xB1,  0x9C,  0x90,
0x29,  0xB3,  0xF4,  0x87,  0x55,  0x93,  0x0E,  0x86,
0x77,  0xF2,  0xA0,  0x35,  0xB5,  0xFC,  0xAB,  0x88,
0x52,  0x69,  0x5D,  0xA9,  0x4C,  0x58,  0xFE,  0x2F,
0x02,  0x22,  0x03,  0xE6,  0x8F,  0xF6,  0x42,  0x8A,
0xFB,  0x30,  0x40,  0x59,  0x84,  0x11,  0x17,  0xD7,
0x05,  0xB0,  0xE5,  0x1C,  0x19,  0x5B,  0xEE,  0x10,
0x18,  0x3D,  0x53,  0x45,  0xDE,  0x0C,  0xCB,  0x26,
0x50,  0xDA,  0xA7,  0xC6,  0xD1,  0xD3,  0x64,  0x73,
0xCE,  0x47,  0xEC,  0xAA,  0x1D,  0x7F,  0xF7,  0xE9,
0xFA,  0x82,  0xC5,  0xF3,  0xCA,  0x41,  0x0D,  0x6B,
0x46,  0x67,  0xC7,  0x2D,  0xFD,  0xE7,  0x8C,  0x60,
0xA6,  0x3B,  0x25,  0x6E,  0x3A,  0x6F,  0xD6,  0x14,
0x9D,  0xD0,  0x39,  0xD5,  0x49,  0x1E,  0xC1,  0x1F,
0x12,  0x61,  0xD2,  0x7B,  0xD9,  0xEB,  0x62,  0x66,
0xBE,  0xB4,  0x7D,  0xB6,  0xBA,  0x1B,  0xF1,  0x98,
0x37,  0xB8,  0xB2,  0x68,  0xCC,  0x2B,  0x2E,  0xC9,
0xB7,  0x81,  0x4E,  0xBD,  0xC3,  0xDB,  0x72,  0x3C,
0xCD,  0x3E,  0x20,  0x65,  0xBC,  0x1A,  0x80,  0x96,
0x6D,  0xA3,  0x78,  0x0A,  0x33,  0xC4,  0x21,  0x06,
0x91,  0xCF,  0x2C,  0xE1,  0x8D,  0x8B,  0x57,  0x36,
]

base16Table = "A3Cw6Gb0OZWPU52s"

def Base16Encode(inputStr):
    outStr1 = ""
    outStr2 = ""
    for i in inputStr:
        val = ord(i)
        outStr1 += base16Table[(val >> 4) & 0xf]
        outStr2 = base16Table[(val) & 0xf] + outStr2
    return outStr1 + outStr2

def Base16Decode(inputStr):
    outStr = ""
    for i in range(0,len(inputStr) / 2):
        v1 = 0
        v2 = 0
        val1 = inputStr[i]
        val2 = inputStr[len(inputStr) - 1 - i]
        for j in range(0,len(base16Table)):
            if val1 == base16Table[j]:
                v1 = j
            if val2 == base16Table[j]:
                v2 = j
        outStr += chr((v1 << 4) | v2)
    return outStr


def EncryptFunc1(decStr):
    encStr = ""
    for i in decStr:
        val = ord(i)
        val = table1[val]
        val = val ^ 0x22
        encStr += chr(val)
    return Base16Encode(encStr)

def DecryptFunc1(encStr):
    encStr = Base16Decode(encStr)
    decStr = ""
    for i in encStr:
        val = ord(i)
        val = val ^ 0x22
        val = detable1[val]
        decStr += chr(val)    
    return decStr

def EncryptFunc2(decStr):
    encStr = ""
    for i in decStr:
        val = ord(i)
        val = table2[val]
        val = val ^ 0x11
        encStr += chr(val)
    return Base16Encode(encStr)

def DecryptFunc2(encStr):
    encStr = Base16Decode(encStr)
    decStr = ""
    for i in encStr:
        val = ord(i)
        val = val ^ 0x11
        val = detable2[val]
        decStr += chr(val)
    return decStr

#serial:"C0ngRa7U1AtIoN2U"
def EncryptFunc3(decStr):
    encStr = ""
  #  print "Start : " + decStr
    #左移一位
    decStr = decStr[1:] + decStr[0:1]
  #  print "Left 1 : " + decStr
    # 查表
    for i in decStr:
        val = ord(i)
        val = table3[val]
        encStr += chr(val)
    decStr = encStr
    encStr = ""
  #  print "Select Table : " + decStr
    #高低4位互换
    for i in decStr:
        val = ord(i)
        val1 = (val & 0xf) << 4
        val2 = (val &0xf0) >> 4
        val = 0xff & (val1 | val2)
        encStr += chr(val)
    decStr = encStr
  #  print "change offset : " + decStr
    encStr = ""
    #每4字节异或
    key = 0x2333AE83
    for i in range(0,4):
        encStr += chr(ord(decStr[i*4+0:i*4+1]) ^ (key & 0xff))
        encStr += chr(ord(decStr[i*4+1:i*4+2]) ^ ((key >> 8) & 0xff))
        encStr += chr(ord(decStr[i*4+2:i*4+3]) ^ ((key >> 16) & 0xff))
        encStr += chr(ord(decStr[i*4+3:i*4+4]) ^ ((key >> 24) & 0xff))
    decStr = encStr
  #  print "4 xor : " + decStr
    encStr = ""
    #前后字节互换
    for i in range(0,len(decStr) / 2):
        encStr += decStr[i*2 + 1]
        encStr += decStr[i*2]
    if len(decStr) % 2 == 1:
        encStr += decStr[len(decStr - 1) :]
    decStr = encStr
    encStr = ""
  #  print "change behind : " + decStr
    # 查表
    for i in decStr:
        val = ord(i)
        val = table3[val]
        encStr += chr(val)
    decStr = encStr
  #  print "select table : " + decStr
    #左移一位
    encStr = decStr[1:] + decStr[0:1]
  #  print "Left 1 : " + encStr
    return Base16Encode(encStr)

def DecryptFunc3(encStr):
    decStr = ""
    encStr = Base16Decode(encStr)
 #   print ""
 #   print encStr
    #右移一位
    encStr = encStr[len(encStr) - 1:] + encStr[:len(encStr) - 1]
 #   print encStr
    # 查表
    for i in encStr:
        val = ord(i)
        val = detable3[val]
        decStr += chr(val)
    encStr = decStr
    decStr = ""
 #   print encStr

    #前后字节互换
    for i in range(0,len(encStr) / 2):
        decStr += encStr[i*2 + 1]
        decStr += encStr[i*2]
    if len(encStr) % 2 == 1:
        decStr += encStr[len(encStr - 1) :]
    encStr = decStr
    decStr = ""
 #   print encStr

    # 每4字节异或
    key = 0x2333AE83
    for i in range(0, 4):
        decStr += chr(ord(encStr[i * 4 + 0:i * 4 + 1]) ^ (key & 0xff))
        decStr += chr(ord(encStr[i * 4 + 1:i * 4 + 2]) ^ ((key >> 8) & 0xff))
        decStr += chr(ord(encStr[i * 4 + 2:i * 4 + 3]) ^ ((key >> 16) & 0xff))
        decStr += chr(ord(encStr[i * 4 + 3:i * 4 + 4]) ^ ((key >> 24) & 0xff))

    encStr = decStr
    decStr = ""
 #   print encStr

    #高低4位互换
    for i in encStr:
        val = ord(i)
        val1 = (val & 0xf) << 4
        val2 = (val &0xf0) >> 4
        val = 0xff & (val1 | val2)
        decStr += chr(val)
    encStr = decStr
    decStr = ""
 #   print encStr

    # 查表
    for i in encStr:
        val = ord(i)
        val = detable3[val]
        decStr += chr(val)
    encStr = decStr
 #   print encStr

    #右移一位
    decStr = encStr[len(encStr) - 1:] + encStr[:len(encStr) - 1]
#    print encStr

    return decStr

print EncryptFunc3("C0ngRa7U1AtIoN2U")
print DecryptFunc3(EncryptFunc3("C0ngRa7U1AtIoN2U"))

# print "lkdakjudajndn  1:"
# print EncryptFunc1("lkdakjudajndn")
# print DecryptFunc1(EncryptFunc1("lkdakjudajndn"))
#
# print "(Ljava/lang/String;)I   2:"
# print EncryptFunc2("(Ljava/lang/String;)I")
# print DecryptFunc2(EncryptFunc2("(Ljava/lang/String;)I"))
#
# print "com/rorschach/executetable/MainActivity    1:"
# print EncryptFunc1("com/rorschach/executetable/MainActivity")
# print DecryptFunc1(EncryptFunc1("com/rorschach/executetable/MainActivity"))
#
# print "/data/data/com.rorschach.executetable/lib/libexecute_table.so    2:"
# print EncryptFunc2("/data/data/com.rorschach.executetable/lib/libexecute_table.so")
# print DecryptFunc2(EncryptFunc2("/data/data/com.rorschach.executetable/lib/libexecute_table.so"))


# print "libexecute_table.so    2:"
# print EncryptFunc2("libexecute_table.so")
# print DecryptFunc2(EncryptFunc2("libexecute_table.so"))
#
# print "/proc/self/status    2:"
# print EncryptFunc2("/proc/self/status")
# print DecryptFunc2(EncryptFunc2("/proc/self/status"))
#
# print "racerPid   1:"
# print EncryptFunc1("racerPid")
# print DecryptFunc1(EncryptFunc1("racerPid"))
#
# print "/proc/self/maps    2:"
# print EncryptFunc2("/proc/self/maps")
# print DecryptFunc2(EncryptFunc2("/proc/self/maps"))
#
# print "%x-%x   1:"
# print EncryptFunc1("%x-%x")
# print DecryptFunc1(EncryptFunc1("%x-%x"))
#
# print "%*s%d  1:"
# print EncryptFunc1("%*s%d")
# print DecryptFunc1(EncryptFunc1("%*s%d"))