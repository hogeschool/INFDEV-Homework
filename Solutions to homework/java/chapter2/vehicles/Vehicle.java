package chapter2.vehicles;


import chapter2.fuels.Fuel;
import chapter2.fuels.Gasoline;

public interface Vehicle {
    Fuel tank = new Gasoline(0);

    public boolean loadFuel(Fuel fuel);
    public boolean move();
}
