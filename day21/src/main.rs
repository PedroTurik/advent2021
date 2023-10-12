use std::cmp::min;

fn main() {
    let mut die: usize = 1;
    let mut p1: usize = 6;
    let mut p1_points: usize = 0;
    let mut p2: usize = 8;
    let mut p2_points: usize = 0;

    let mut plays: usize = 0;

    loop {
        p1 = (p1 + (3 * (die + 1))) % 10;
        die = (die + 3) % 100;
        p1_points += p1 + 1;
        if p1_points > 1000 {
            break;
        }

        p2 = (p2 + (3 * (die + 1))) % 10;
        die = (die + 3) % 100;
        p2_points += p2 + 1;
        if p2_points > 1000 {
            break;
        }

        plays += 1;
    }

    println!("{}", plays * min(p1_points, p2_points));
}
