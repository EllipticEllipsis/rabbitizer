/* SPDX-FileCopyrightText: © 2022 Decompollaborate */
/* SPDX-License-Identifier: MIT */

mod access_type_enum;
mod instr_category_enum;
mod instr_id_enum;
mod operand_type_enum;
mod registers_enum;
mod instr_suffix_enum;
mod instruction;
mod instr_descriptor;
mod abi_enum;
mod registers_methods;
mod opereand_type;
pub mod config;
pub mod utils;

pub use access_type_enum::AccessType;
pub use instr_category_enum::InstrCategory;
pub use instr_id_enum::InstrId;
pub use operand_type_enum::OperandType;
pub use registers_enum::registers;
pub use instr_suffix_enum::InstrSuffix;
pub use instruction::Instruction;
pub use instr_descriptor::InstrDescriptor;
pub use abi_enum::Abi;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(
            instruction::Instruction::new(0x8D4A7E18, 0x80000000, instr_category_enum::InstrCategory::CPU).disassemble(None, 0),
            "lw          $t2, 0x7E18($t2)".to_string()
        );
    }

    #[test]
    fn test_get_operand_type() {
        let instr = instruction::Instruction::new(0x8D4A7E18, 0x80000000, instr_category_enum::InstrCategory::CPU);
        let operand = instr.get_operand_type(0);

        assert_eq!(
            operand.disassemble(instr, None),
            "$t2".to_string()
        );
    }

    #[test]
    fn test_operands_slice() {
        let instr = instruction::Instruction::new(0x8D4A7E18, 0x80000000, instr_category_enum::InstrCategory::CPU);
        let operands_slice= instr.get_operands_slice();

        assert_eq!(operands_slice.len(), 2);
    }
}
