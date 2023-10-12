public class Beacon {
    public int x;
    public int y;
    public int z;

    public Beacon(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public String toString() {
        return String.format("(x:%d, y:%d, z:%d)", x, y, z);
    }
}
