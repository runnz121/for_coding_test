import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class samplejava {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // python 의 sys.stdin.readline
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); //python의 sys.stdin.outline

		int n = Integer.parseInt(br.readLine());
		bw.write(n);
		StringTokenizer st = new StringTokenizer(br.readLine()); // 공백 구분(python 의 input.split()

	}
}
