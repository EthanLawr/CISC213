import java.util.Vector;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class WeatherVectorApp {

    private static Vector<Double> airTemp = new Vector<Double>();
    private static File airTempFile = new File("CISC213JCFExercise.csv");
    private static Scanner aTFileScanner;

    public static void main(String[] args) throws FileNotFoundException {
	aTFileScanner = new Scanner(airTempFile);
	readFile();
	airTempStats();
	aTFileScanner.close();
    }
    
    private static void readFile() {
	System.out.println("Size of airTemp Vector before load: "
			   + airTemp.size());
	while(aTFileScanner.hasNext()) {
	    airTemp.addElement(aTFileScanner.nextDouble());
	}
	System.out.printf("Size of airTemp Vector after load: %,d\n",
			  airTemp.size());
    }

    private static void airTempStats() {
	double read = airTemp.get(0);
	double max = read;
	double total = read;
	double min = read;
	for(int i = 1; i < airTemp.size(); i++) {
	    read = airTemp.get(i);
	    if(read < min) min = read;
	    if(read > max) max = read;
	    total += read;
	}
	System.out.println("Minimum air temperature in Celsius: " +
			   min);
	System.out.println("Maximum air temperature in Celsius: " +
			   max);
	System.out.printf("Average air temperature in Celsius: %.2f\n",
			   total/airTemp.size());
    }
}