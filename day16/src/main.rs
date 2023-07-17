mod parser;
use parser::PacketParser;
use std::fs;

fn hex_to_bin(hex: &str) -> String {
    hex.chars().map(to_binary).collect()
}

fn to_binary(c: char) -> &'static str {
    match c {
        '0' => "0000",
        '1' => "0001",
        '2' => "0010",
        '3' => "0011",
        '4' => "0100",
        '5' => "0101",
        '6' => "0110",
        '7' => "0111",
        '8' => "1000",
        '9' => "1001",
        'A' => "1010",
        'B' => "1011",
        'C' => "1100",
        'D' => "1101",
        'E' => "1110",
        'F' => "1111",
        _ => "",
    }
}

fn all_parts(bin: String) {
    let mut parser = PacketParser::new(bin);
    let ans2 = parser.parse_packet();
    println!("part1: {}  part2: {}", parser.total_ver, ans2);
}

fn main() {
    let bit_transmission: String = fs::read_to_string("input.txt").unwrap().trim().to_owned();

    all_parts(hex_to_bin(&bit_transmission));
}
