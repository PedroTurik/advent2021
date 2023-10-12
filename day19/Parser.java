import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Parser {
    public static Map<Integer, List<Beacon>> parse(String input) throws FileNotFoundException {
        var scanners = new HashMap<Integer, List<Beacon>>();
        var file = new File(input);

        var counter = 0;

        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                scanner.nextLine();
                String row;
                var beaconsList = new ArrayList<Beacon>();
                while (scanner.hasNextLine() && !(row = scanner.nextLine()).isEmpty()) {
                    var beacon = row.split(",");
                    var beaconX = Integer.parseInt(beacon[0]);
                    var beaconY = Integer.parseInt(beacon[1]);
                    var beaconZ = Integer.parseInt(beacon[2]);

                    beaconsList.add(new Beacon(beaconX, beaconY, beaconZ));

                }
                scanners.put(counter, beaconsList);
                counter++;
            }
        }

        return scanners;
    }
}
