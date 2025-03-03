/* SPDX-FileCopyrightText: © 2022 Decompollaborate */
/* SPDX-License-Identifier: MIT */

use crate::registers_enum;

extern "C" {
    pub static mut RabbitizerRegister_GprO32_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_GprN32_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop0_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop1O32_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop1N32_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop1N64_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop1Control_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_Cop2_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_RspGpr_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_RspCop0_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_RspCop2_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_RspCop2Control_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_RspVector_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_R5900VF_Names: [[*const core::ffi::c_char; 2usize]; 0usize];
    pub static mut RabbitizerRegister_R5900VI_Names: [[*const core::ffi::c_char; 2usize]; 0usize];

    /*
    pub fn RabbitizerRegister_getNameGpr(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameCop0(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameCop1(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameCop1Control(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameCop2(reg_value: u8) -> *const core::ffi::c_char;

    pub fn RabbitizerRegister_getNameRspGpr(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameRspCop0(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameRspCop2(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameRspCop2Control(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameRspVector(reg_value: u8) -> *const core::ffi::c_char;

    pub fn RabbitizerRegister_getNameR5900VF(reg_value: u8) -> *const core::ffi::c_char;
    pub fn RabbitizerRegister_getNameR5900VI(reg_value: u8) -> *const core::ffi::c_char;
    */
}

impl registers_enum::registers::GprO32 {
    pub fn name(&self) -> &'static str {
        let reg_value: u32 = (*self).into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_GprO32_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::GprN32 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_GprN32_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::Cop0 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop0_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        match *self {
            registers_enum::registers::Cop0::Reserved07 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved21 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved22 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved23 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved24 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved25 => {
                return true;
            }
            registers_enum::registers::Cop0::Reserved31 => {
                return true;
            }
            _ => {
                return false;
            }
        }
    }
}

impl registers_enum::registers::Cop1O32 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop1O32_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::Cop1N32 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop1N32_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::Cop1N64 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop1N64_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::Cop1Control {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop1Control_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::Cop2 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_Cop2_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::RspGpr {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_RspGpr_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::RspCop0 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_RspCop0_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::RspCop2 {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_RspCop2_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::RspCop2Control {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_RspCop2Control_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::RspVector {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_RspVector_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::R5900VF {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_R5900VF_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}

impl registers_enum::registers::R5900VI {
    pub fn name(self) -> &'static str {
        let reg_value: u32 = self.into();

        unsafe {
            std::ffi::CStr::from_ptr(RabbitizerRegister_R5900VI_Names[reg_value as usize][1]).to_str().unwrap()
        }
    }

    pub fn is_reserved(&self) -> bool {
        false
    }
}
