pub struct PacketParser {
    bits: Vec<char>,
    position: usize,
    read_position: usize,
    ch: char,
    pub total_ver: usize,
}

impl PacketParser {
    pub fn new(bits: String) -> PacketParser {
        let mut parser = PacketParser {
            bits: bits.chars().collect(),
            position: 0,
            read_position: 0,
            ch: ' ',
            total_ver: 0,
        };

        parser.read_char();

        parser
    }

    fn read_literal(&mut self) -> usize {
        let mut binary_literal = String::new();
        let mut is_final = false;
        while !is_final {
            if self.ch == '0' {
                is_final = true
            }

            self.read_char();
            for _ in 0..4 {
                binary_literal.push(self.ch);
                self.read_char();
            }
        }

        usize::from_str_radix(&binary_literal, 2).unwrap()
    }

    fn handle_operation(values: Vec<usize>, operator: usize) -> usize {
        match operator {
            0 => values.iter().sum(),
            1 => values.iter().product(),
            2 => *values.iter().min().unwrap(),
            3 => *values.iter().max().unwrap(),
            5 => {
                if values[0] > values[1] {
                    1
                } else {
                    0
                }
            }
            6 => {
                if values[0] < values[1] {
                    1
                } else {
                    0
                }
            }
            7 => {
                if values[0] == values[1] {
                    1
                } else {
                    0
                }
            }
            _ => panic!(),
        }
    }

    fn read_by_length(&mut self, operator: usize) -> usize {
        let size = self.get_usize_from_bin(15);
        let prev_pos = self.position;
        let mut res = Vec::new();
        while self.position < prev_pos + size {
            res.push(self.parse_packet());
        }

        Self::handle_operation(res, operator)
    }

    fn read_by_npackets(&mut self, operator: usize) -> usize {
        let size = self.get_usize_from_bin(11);
        let mut res = Vec::new();
        for _ in 0..size {
            res.push(self.parse_packet());
        }

        Self::handle_operation(res, operator)
    }

    fn read_operator(&mut self, operator: usize) -> usize {
        let size_type = self.ch;
        self.read_char();

        match size_type {
            '0' => self.read_by_length(operator),
            '1' => self.read_by_npackets(operator),
            _ => panic!(),
        }
    }

    pub fn parse_packet(&mut self) -> usize {
        let (ver, type_id) = self.read_header();
        self.total_ver += ver;

        match type_id {
            4 => self.read_literal(),
            x => self.read_operator(x),
        }
    }

    fn read_header(&mut self) -> (usize, usize) {
        (self.get_usize_from_bin(3), self.get_usize_from_bin(3))
    }

    fn read_char(&mut self) {
        if self.read_position >= self.bits.len() {
            self.ch = ' ';
        } else {
            self.ch = self.bits[self.read_position];
        }

        self.position = self.read_position;
        self.read_position += 1;
    }

    fn get_usize_from_bin(&mut self, n: usize) -> usize {
        let mut bin = String::new();
        for _ in 0..n {
            bin.push(self.ch);
            self.read_char();
        }

        usize::from_str_radix(&bin, 2).unwrap()
    }
}
