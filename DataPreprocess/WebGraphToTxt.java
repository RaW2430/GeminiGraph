import it.unimi.dsi.webgraph.ImmutableGraph;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class GraphToCSV {
    public static void main(String[] args) {
        String graphPath = "cnr-2000"; // 不带扩展名
        String outputFile = "cnr-2000.csv";

        try {
            // 加载图
            ImmutableGraph graph = ImmutableGraph.load(graphPath);
            int numNodes = graph.numNodes();

            System.out.println("Graph loaded with " + numNodes + " nodes.");
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile));
            writer.write("source,target\n"); // CSV 头

            for (int i = 0; i < numNodes; i++) {
                int[] successors = graph.successorArray(i);
                for (int j = 0; j < successors.length; j++) {
                    writer.write(i + "," + successors[j] + "\n");
                }

                // 可选：显示进度
                if (i % 100000 == 0) {
                    System.out.println("Processed node " + i);
                }
            }

            writer.close();
            System.out.println("Export finished to " + outputFile);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
import it.unimi.dsi.webgraph.ImmutableGraph;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class GraphToCSV {
    public static void main(String[] args) {
        String graphPath = "cnr-2000"; // 不带扩展名
        String outputFile = "cnr-2000.csv";

        try {
            // 加载图
            ImmutableGraph graph = ImmutableGraph.load(graphPath);
            int numNodes = graph.numNodes();

            System.out.println("Graph loaded with " + numNodes + " nodes.");
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile));
            writer.write("source,target\n"); // CSV 头

            for (int i = 0; i < numNodes; i++) {
                int[] successors = graph.successorArray(i);
                for (int j = 0; j < successors.length; j++) {
                    writer.write(i + "," + successors[j] + "\n");
                }

                // 可选：显示进度
                if (i % 100000 == 0) {
                    System.out.println("Processed node " + i);
                }
            }

            writer.close();
            System.out.println("Export finished to " + outputFile);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
